# 面试题53，题目一：数字在排序数组中出现的次数

def get_first_k(nums, k, start, end) -> int:
    if start > end:
        return -1
    mid_index = (start + end) // 2
    mid_num = nums[mid_index]

    if mid_num == k:
        if (mid_index > 0 and nums[mid_index - 1] != k) or mid_index == 0:
            return mid_index
        else:
            end = mid_index - 1
    elif  mid_num < k:
        start = mid_index + 1
    else:
        end = mid_index - 1
    return get_first_k(nums, k, start, end)

def get_last_k(nums, k, start, end) -> int:
    if start > end:
        return -1
    mid_index = (start + end) // 2
    mid_num = nums[mid_index]

    if mid_num == k:
        if (mid_index < len(nums) - 1 and nums[mid_index + 1] != k) or mid_index == len(nums) - 1:
            return mid_index
        else:
            start = mid_index + 1
    elif mid_num < k:
        start = mid_index + 1
    else:
        end = mid_index - 1
    return get_last_k(nums, k, start, end)

def get_num_of_k(nums, k):
    start = get_first_k(nums, k, 0, len(nums) - 1)
    end = get_last_k(nums, k, 0, len(nums) - 1)
    if start >= 0 and end >= 0:
        return end - start + 1
    else:
        return 0

if __name__ == '__main__':
    data = [1,2,3,3,3,3,4,5]
    k = 5
    print(get_num_of_k(data, k))