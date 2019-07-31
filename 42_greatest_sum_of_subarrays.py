# 面试题42：连续子数组的最大和

def find_max_sum(array):
    if not array:
        return None

    for i in range(1, len(array)):
        if array[i - 1] >= 0:
            array[i] = array[i - 1] + array[i]

    return max(array)

if __name__ == '__main__':
    nums = [1,-2,3,10,-4,7,2,-5]
    print(find_max_sum(nums))
