# 面试题47：礼物的最大价值

def get_max_value(values):
    if not values:
        return 0

    for i in range(1, len(values[0])):
        values[0][i] += values[0][i - 1]
    for i in range(1, len(values)):
        values[i][0] += values[i - 1][0]

    for i in range(1, len(values)):
        for j in range(1, len(values[0])):
            values[i][j] += max(values[i-1][j], values[i][j-1])
    return values[-1][-1]



if __name__ == '__main__':
    values = [
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]
    ]
    print(get_max_value(values))