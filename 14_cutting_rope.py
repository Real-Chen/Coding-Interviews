# 面试题14：剪绳子

# 动态规划解法
def cut_rope_dynamic_programming(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    product = [0] * (n+1)
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3
    for i in range(4, n+1):
        max_product = 0
        for j in range(1, i//2 + 1):
            one_product = product[j] * product[i-j]
            if one_product > max_product:
                max_product = one_product
            product[i] = max_product
    return product[-1]

# 贪心算法
def cut_rope_greedy_algorithm(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    time_of_3 = n // 3
    remain = n % 3
    if remain == 1:
        time_of_3 -= 1
        remain = 4
    return 3 ** time_of_3 * remain

if __name__ == '__main__':
    n = 8
    print(cut_rope_dynamic_programming(n))
    print(cut_rope_greedy_algorithm(n))