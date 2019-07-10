# 面试题21：调整数组顺序使奇数位于偶数前面
def reorder_odd_even(array):
    if not array:
        return
    i = 0
    j = len(array) - 1
    while i < j:
        if i < j and not isEven(array[i]):
            i += 1
        if i < j and isEven(array[j]):
            j -= 1
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
    return array

def isEven(n:int):
    return (n & 1) == 0

if __name__ == '__main__':
    unorder_array = [1, 2, 3, 4, 5, 6, 7]
    print(reorder_odd_even(unorder_array))