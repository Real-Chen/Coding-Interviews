# 面试题10 斐波那契数列

# 递归实现
def Fibonacci_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci_recursive(n - 1) + Fibonacci_recursive(n - 2)

# 循环实现
def Fibonacci_iterative(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    num1 = 0
    num2 = 1
    num3 = 1
    for _ in range(n-2):
        num1 = num2
        num2 = num3
        num3 = num1 + num2
    return num3

if __name__ == '__main__':
    n = 10
    print(Fibonacci_recursive(n))
    print(Fibonacci_iterative(n))

