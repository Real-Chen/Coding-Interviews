# 面试题50：第一次只出现一次的字符
def find_not_repeating_char(str):
    ch_d = {}
    for ch in str:
        if ch in ch_d:
            ch_d[ch] += 1
        else:
            ch_d[ch] = 1
    for ch in str:
        if ch_d[ch] == 1:
            return ch
    return None

if __name__ == '__main__':
    sample = 'abaccdeff'
    print(find_not_repeating_char(sample))