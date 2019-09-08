# 面试题56-1：数组中只出现一次的数字

def find_nums_appear_once(nums):
    if not nums or len(nums) < 2:
        return -1, -1
    EOR = 0
    for num in nums:
        EOR ^= num
    index = find_first_bit_is_1(EOR)
    num1 = num2 = 0
    for num in nums:
        if is_bit_1(num, index):
            num1 ^= num
        else:
            num2 ^= num
    return num1, num2

def find_first_bit_is_1(num):
    index_bit = 0
    while num & 1 == 0:
        num >> 1
        index_bit += 1
    return index_bit

def is_bit_1(num, index_bit):
    num = num >> index_bit
    return num & 1

if __name__ == '__main__':
    nums = [2,4,4,6,3,2,5,5]
    print(find_nums_appear_once(nums))