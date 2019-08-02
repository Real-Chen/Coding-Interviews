# 面试题45：把数组排成最小的数
from functools import cmp_to_key

def mycmp(a, b):
    if a+b < b+a:
        return -1
    else:
        return 1

def print_min_number(numbers):
    numbers = list(map(str, numbers))
    if not numbers:
        return ""
    numbers.sort(key=cmp_to_key(mycmp))
    return ''.join(numbers)

if __name__ == '__main__':
    numbers = [3, 32, 321]
    print(print_min_number(numbers))