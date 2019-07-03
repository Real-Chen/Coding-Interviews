# 面试题4：二维数组中的查找
# 思路：从右上角开始查找，不断地缩小查找范围
def find(input_array, target_num):
    rows = len(input_array)
    cols = len(input_array[0])

    row = 0
    col = cols - 1
    while (col >= 0 and row < rows):
        if input_array[col][row] == target_num:
            return True
        elif input_array[col][row] < target_num:
            row += 1
        else:
            col -= 1
    return False

if __name__ == '__main__':
    input_array = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    target_num = 7
    print(find(input_array, target_num))