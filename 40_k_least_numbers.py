# 面试题40：最小的k个数

# 为了学习堆，自己写个堆吧！
class Heap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        index = len(self.heap)
        self.heap.append(val)
        parent = (index - 1) // 2
        while parent >= 0 and self.heap[parent] < self.heap[index]:
            tmp = self.heap[index]
            self.heap[index] = self.heap[parent]
            self.heap[parent] = tmp
            index = parent
            parent = (index - 1) // 2

    def pop(self):
        if not self.heap:
            return None
        tmp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = tmp
        max = self.heap.pop(-1)
        self.shift_down()
        return max

    def shift_down(self):
        index = 0
        left = index * 2 + 1
        right = index * 2 + 2
        flag = (left < len(self.heap) and self.heap[left] > self.heap[index]) \
               or (right < len(self.heap) and self.heap[right] > self.heap[index])

        while flag:
            if right < len(self.heap):
                bigger_index = left if self.heap[left] >= self.heap[right] else right
            else:
                bigger_index = left

            tmp = self.heap[index]
            self.heap[index] = self.heap[bigger_index]
            self.heap[bigger_index] = tmp

            index = bigger_index
            left = index * 2 + 1
            right = index * 2 + 2
            flag = (left < len(self.heap) and self.heap[left] > self.heap[index]) \
                   or (right < len(self.heap) and self.heap[right] > self.heap[index])

# k堆，容量限制为k的堆
# 这里为了重新学一下python面向对象的知识
class KHeap(Heap):
    def __init__(self, k):
        Heap.__init__(self)
        self.k = k

    def insert(self, val):
        if len(self.heap) < self.k:
            super().insert(val)
        elif val < self.heap[0]:
            self.heap[0] = val
            self.shift_down()


# 利用堆求最小个k值
def get_least_numbers(nums: list, k: int) -> list:
    if k > len(nums) or k <= 0:
        return []
    k_heap = KHeap(k)
    for num in nums:
        k_heap.insert(num)
    return sorted(k_heap.heap)

if __name__ == '__main__':
    nums = [4,5,1,6,2,7,3,8]
    k = 4
    print(get_least_numbers(nums, k))
