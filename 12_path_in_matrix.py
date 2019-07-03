# 面试12：矩阵中的路径

def has_path(matrix, target_str) -> bool:
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if has_path_core(matrix, visited, i, j, 0, target_str):
                return True
    return False

def has_path_core(matrix, visited, row, col, ch_index, str):
    if ch_index >= len(str):
        return True
    has_path = False
    if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) \
            and matrix[row][col] == str[ch_index] and not visited[row][col]:
        ch_index += 1
        visited[row][col] = True
        has_path = has_path_core(matrix, visited, row - 1, col, ch_index, str) or \
                   has_path_core(matrix, visited, row + 1, col, ch_index, str) or \
                   has_path_core(matrix, visited, row, col - 1, ch_index, str) or \
                   has_path_core(matrix, visited, row, col + 1, ch_index, str)
        if not has_path:
            ch_index -= 1
            visited[row][col] = False
    return has_path


if __name__ == '__main__':
    matrix = [
        ['a', 'b', 't', 'g'],
        ['c', 'f', 'c', 's'],
        ['j', 'd', 'e', 'h'],
    ]
    target_str = "bfce"
    print(has_path(matrix, target_str))