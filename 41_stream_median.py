# 面试题41：数据流中的中位数

import numpy as np

# 最大堆
class maxHeap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.shift_up()

    def shift_up(self):
        index = len(self.heap) - 1
        parent = (index - 1) // 2
        while parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def pop(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
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

            self.heap[index], self.heap[bigger_index] = self.heap[bigger_index], self.heap[index]

            index = bigger_index
            left = index * 2 + 1
            right = index * 2 + 2
            flag = (left < len(self.heap) and self.heap[left] > self.heap[index]) \
                   or (right < len(self.heap) and self.heap[right] > self.heap[index])

# 最小堆
class minHeap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.shift_up()

    def shift_up(self):
        index = len(self.heap) - 1
        parent = (index - 1) // 2
        while parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def pop(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min = self.heap.pop(-1)
        self.shift_down()
        return min

    def shift_down(self):
        index = 0
        left = index * 2 + 1
        right = index * 2 + 2
        flag = (left < len(self.heap) and self.heap[left] < self.heap[index]) \
               or (right < len(self.heap) and self.heap[right] < self.heap[index])

        while flag:
            if right < len(self.heap):
                bigger_index = left if self.heap[left] <= self.heap[right] else right
            else:
                bigger_index = left

            self.heap[index], self.heap[bigger_index] = self.heap[bigger_index], self.heap[index]

            index = bigger_index
            left = index * 2 + 1
            right = index * 2 + 2
            flag = (left < len(self.heap) and self.heap[left] < self.heap[index]) \
                   or (right < len(self.heap) and self.heap[right] < self.heap[index])


# 寻找中位数
class mergeHeap():
    def __init__(self):
        self.left_heap = maxHeap()
        self.right_heap = minHeap()
        self.size = 0

    def insert(self, val):
        if not self.left_heap.heap and not self.right_heap.heap:
            self.left_heap.insert(val)
        elif self.size % 2:
            if val < self.left_heap.heap[0]:
                big_val = self.left_heap.pop()
                self.left_heap.insert(val)
                self.right_heap.insert(big_val)
            else:
                self.right_heap.insert(val)
        else:
            if val > self.right_heap.heap[0]:
                small_val = self.right_heap.pop()
                self.left_heap.insert(small_val)
                self.right_heap.insert(val)
            else:
                self.left_heap.insert(val)
        self.size += 1

    def get_median(self):
        if not self.size:
            return None
        if self.size % 2:
            return self.left_heap.heap[0]
        else:
            return (self.left_heap.heap[0] + self.right_heap.heap[0]) / 2



if __name__ == '__main__':
    nums = np.random.randint(50, size=20)
    median_heap = mergeHeap()
    for num in nums:
        median_heap.insert(num)
        print(num, median_heap.get_median())
        print(median_heap.left_heap.heap, median_heap.right_heap.heap)
