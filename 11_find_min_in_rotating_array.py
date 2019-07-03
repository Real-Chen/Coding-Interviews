# 面试题11：旋转数组的最小数字

def find_min_recursive(nums):
    if not nums:
        return
    if nums[0] < nums[-1]:
        return nums[0]
    if len(nums) <= 2:
        return nums[-1]
    index_mid = len(nums) // 2
    if nums[index_mid] >= nums[0]:
        return find_min_recursive(nums[index_mid:])
    else:
        return find_min_recursive(nums[:index_mid+1])

def find_min(nums):
    if not nums:
        return
    if nums[0] < nums[-1]:
        return nums[0]
    index1 = 0
    index2 = len(nums) - 1
    while index2 - index1 > 1:
        index_mid = (index1 + index2) // 2
        if nums[index_mid] >= nums[index1]:
            index1 = index_mid
        else:
            index2 = index_mid
    return nums[index2]

if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums))
    print(find_min_recursive(nums))