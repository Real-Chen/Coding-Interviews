# 面试题29：顺时针打印矩阵

# 开启循环
def print_matrix(matrix, cols, rows, start):
    end_x = rows - start - 1
    end_y = cols - start - 1
    for i in range(start, end_x+1):
        print(matrix[start][i])
    if start < end_y:
        for i in range(start+1, end_y+1):
            print(matrix[i][end_x])
    if start < end_x and start < end_y:
        for i in range(end_x-1, start-1, -1):
            print(matrix[end_y][i])
    if start < end_x and start < end_y - 1:
        for i in range(end_y-1, start, -1):
            print(matrix[i][start])
    start += 1
    if cols > 2 * start and rows > 2 * start:
        print_matrix(matrix, cols, rows, start)

if __name__ == '__main__':
    vals_matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    print_matrix(vals_matrix, len(vals_matrix), len(vals_matrix[0]), 0)