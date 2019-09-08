# 面试题53-2:0~n-1中缺失的数字

def get_missing_number(nums):
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid_index = (left + right) // 2
        if nums[mid_index] != mid_index:
            if mid_index == 0 or nums[mid_index - 1] == mid_index - 1:
                return mid_index
            right = mid_index - 1
        else:
            left = mid_index + 1
    if left == len(nums):
        return left
    return -1

if __name__ == '__main__':
    nums = [0,1,2,3,4,5,7]
    print(get_missing_number(nums))