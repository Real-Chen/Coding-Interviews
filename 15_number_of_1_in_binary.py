# 二进制中1的个数

# 负数陷入死循环写法
def num_of_1_sol1(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count

# 常规写法
# 注:python的int型，没有位数限制还是会陷入死循环
def num_of_1_sol2(n:int):
    count = 0
    flag = 1
    while flag and flag <= abs(n):
        if n & flag :
            count += 1
        flag = flag << 1
    return count

# 取巧解法
def num_of_1_sol3(n):
    count = 0
    while n:
        count += 1
        n = (n - 1) & n
    return count

if __name__ == '__main__':
    n = 9
    print(num_of_1_sol1(n))
    print(num_of_1_sol2(n))
    print(num_of_1_sol3(n))