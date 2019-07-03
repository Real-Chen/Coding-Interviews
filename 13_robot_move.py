# 面试题13：机器人的运动范围

def move_count(threshold, rows, cols):
    if threshold <= 0 or rows <= 0 or cols <= 0:
        return 0
    visited = [[False] * cols for _ in range(rows)]
    return move_count_core(threshold, 0, 0, rows, cols, visited)

def move_count_core(threshold, row, col, rows, cols, visited):
    count = 0
    if check(threshold, row, col, rows, cols, visited):
        visited[row][col] = True
        count = 1 + \
                move_count_core(threshold, row - 1, col, rows, cols, visited) + \
                move_count_core(threshold, row + 1, col, rows, cols, visited) + \
                move_count_core(threshold, row, col - 1, rows, cols, visited) + \
                move_count_core(threshold, row, col + 1, rows, cols, visited)
    return count

def check(threshold, row, col, rows, cols, visited):
    if row >=0 and row < rows and col >=0 and col< cols and \
            (get_digit_sum(row) + get_digit_sum(col)) <= threshold and \
            not visited[row][col]:
        return True
    else:
        return False
def get_digit_sum(num):
    sum = 0
    while num:
        sum += num % 10
        num = num // 10
    return sum

if __name__ == "__main__":
    print(move_count(15, 100, 1))
    # 更多测试样例可参考《剑指offer》官方github
    # https://github.com/zhulintao/CodingInterviewChinese2/blob/master/13_RobotMove/RobotMove.cpp