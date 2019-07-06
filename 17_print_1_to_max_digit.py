# 面试题10：打印从1到最大的n位数
def print1_to_max(n):
    if n <= 0:
        return
    number = [''] * n
    for i in range(10):
        number[0] = str(i)
        print1_to_max_recursive(number, n, 0)

def print1_to_max_recursive(number, length, index):
    if index == length - 1:
        print(int(''.join(number)))
        return
    for i in range(10):
        number[index+1] = str(i)
        print1_to_max_recursive(number, length, index + 1)

if __name__ == '__main__':
    n = 10
    print1_to_max(3)