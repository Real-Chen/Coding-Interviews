# 面试题43:1~n整数中1出现的次数
# 本题待完善

def num_of_1_between_1_and_N(n):
    if n <= 0:
        return 0
    num = 0
    while n:
        if n % 10 == 1:
            num += 1
        n = n // 10
    return num

def number_of_1(num_str):
    if not str:
        return None
    first = int(num_str[0])
    length = len(num_str)

    if length == 1 and first == 0:
        return 0
    if length == 1 and first > 0:
        return 1

    num_first_digit = 0
    if first > 1:
        num_first_digit = pow(10, length - 1)
    elif first == 1:
        num_first_digit = int(num_str[1:]) + 1

    num_other_digit = first * (length - 1) * pow(10, length - 2)
    num_recursive = num_of_1_between_1_and_N(int(num_str[1:]))
    return num_first_digit + num_other_digit + num_recursive




if __name__ == '__main__':
    num = 21345
    print(number_of_1(str(num)))
