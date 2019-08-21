# 面试题48：最长不含重复字符的子字符串
import string

def get_longest_substring(str):
    position = {}
    for ch in string.ascii_lowercase:
        position[ch] = -1
    cur_length = 0
    max_length = 0
    # 遍历开始动态规划
    for i in range(len(str)):
        pre_index = position[str[i]]
        if position[str[i]] < 0 or (i - pre_index) > cur_length:
            cur_length += 1
        else:
            if cur_length > max_length:
                max_length = cur_length
            cur_length = i - pre_index
        position[str[i]] = i
    if cur_length > max_length:
        max_length = cur_length
    return max_length


if __name__ == '__main__':
    test_sample = "arabcacfr"
    print(get_longest_substring(test_sample))