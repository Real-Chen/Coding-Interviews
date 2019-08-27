# 面试题51：数组中的逆序对

def inverse_pairs(data):
    if not data:
        return 0
    copy = [0] * len(data)
    count = inverse_pairs_core(data, copy, 0, len(data) - 1)
    del copy
    return count

def inverse_pairs_core(data, copy, start, end):
    if start == end:
        copy[start] = data[start]
        return 0
    length = (end- start) // 2
    left = inverse_pairs_core(data, copy, start, start + length)
    right = inverse_pairs_core(data, copy, start + length + 1, end)

    i = start + length
    j = end
    index_copy = end
    count = 0

    while i >= start and j >= start + length + 1:
        if data[i] > data[j]:
            copy[index_copy] = copy [i]
            index_copy -= 1
            i -= 1
            count += j - start - length
        else:
            copy[index_copy] = copy[i]
            index_copy -= 1
            i -= 1
    while i >= start:
        copy[index_copy] = data[i]
        index_copy -= 1
        i -= 1
    while j >= start + length + 1:
        copy[index_copy] = data[j]
        index_copy -= 1
        j -= 1
    return left + right + count

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 7, 6, 5]
    print(inverse_pairs(nums))  # 3
    nums = [6, 5, 4, 3, 2, 1]
    print(inverse_pairs(nums))  # 15
    nums = [1, 2, 3, 4, 5, 6]
    print(inverse_pairs(nums))  # 0
    nums = [1]
    print(inverse_pairs(nums))  # 0
    nums = [1, 2]
    print(inverse_pairs(nums))  # 0
    nums = [2, 1]
    print(inverse_pairs(nums))  # 1