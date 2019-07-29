# 面试题39：数组中出现次数超过一半的数字

# 方法1：基于快排思想的partition算法
def more_than_half_num(nums):
    if not nums:
        return 0
    length = len(nums)
    start = 0
    end = length - 1
    half = length // 2
    index = partition(nums, length, start, end)
    while index != half:
        if index < half:
            index = partition(nums, length, index + 1, end)
        else:
            index = partition(nums, length, start, index - 1)
    mid_num = nums[half]
    if check_more_than_half(nums, length, mid_num):
        return mid_num
    else:
        return 0

def partition(nums, length, start, end):
    num0 = nums[start]
    i = start
    j = end
    while i < j:
        while i < j and nums[j] >= num0:
            j -= 1
        while i < j and nums[i] <= num0:
            i += 1
        if i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        nums[start] = nums[j]
        nums[j] = num0
    return j

def check_more_than_half(nums, length, tar_num):
    count = 0
    for num in nums:
        if num == tar_num:
            count += 1
    if count * 2 > length:
        return True
    else:
        return False

# 方法2：基于数组性质
def more_than_half_num_2(nums):
    if not nums:
        return 0
    count = 1
    count_num = nums[0]
    for num in nums:
        if count == 0:
            count_num = num
            count = 1
        elif count_num == num:
            count += 1
        else:
            count -= 1
    if check_more_than_half(nums, len(nums), count_num):
        return count_num
    else:
        return 0

if __name__ == '__main__':
    array = [1,2,3,2,2,2,5,4,2]
    print(more_than_half_num(array))
    print(more_than_half_num_2(array))