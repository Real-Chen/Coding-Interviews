# 面试题16：数值的整数次方

import datetime
# 常规法
def power(base, exponent):
    if not base:
        return 0
    if exponent < 0:
        return 1 / power_with_unsigned_advanced(base, -exponent)
    else:
        return power_with_unsigned_advanced(base, exponent)

def power_with_unsigned(base, exponent):
    result = 1.0
    for _ in range(exponent):
        result *= base
    return result

# 高效解法
def power_with_unsigned_advanced(base, exponent):
    if exponent == 0:
        return 1.0
    if exponent == 1:
        return base
    result = power_with_unsigned_advanced(base, exponent >> 1)
    result *= result
    if exponent & 1:
        result *= base
    return result

if __name__ == '__main__':
    base = 2
    exponent = 1000

    print(power(2, -1000))
    print(power_with_unsigned(base, exponent))
    print(power_with_unsigned_advanced(base, exponent))