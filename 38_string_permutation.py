# 面试38：字符串全排列

def permutation(raw_str):
    if not raw_str:
        return []
    permutation_strings = []
    for i in range(len(raw_str)):
        late_strings = permutation(raw_str[:i]+raw_str[i+1:])
        if not late_strings:
            permutation_strings.append(raw_str[i])
        else:
            merge_strings = [raw_str[i] + late_string for late_string in late_strings]
            permutation_strings += merge_strings
    return permutation_strings

if __name__ == '__main__':
    raw_str = 'abcd'
    print(permutation(raw_str))