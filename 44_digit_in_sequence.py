# 面试题44：数字序列中某一位的数字

def digits_at_index(index: int) -> int:
    if index < -1:
        return -1
    digits = 1
    while True:
        numbers = count_of_integers(digits)
        if index < numbers * digits:
            return digit_at_index(index, digits)
        index -= digits * numbers
        digits += 1

def digit_at_index(index, digits):
    number = begin_number(digits) + index // digits
    index_from_right = digits - index % digits
    for i in range(1, index_from_right):
        number = number // 10
    return number % 10

def begin_number(digits):
    if digits == 1:
        return 0
    return pow(10, digits - 1)

def count_of_integers(digits):
    if digits == 1:
        return 10
    count = pow(10, digits - 1)
    return 9 * count

if __name__ == '__main__':
    for index in range(200):
        print(digits_at_index(index), end='')