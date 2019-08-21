# 面试题49：丑数

def get_ugly_num(index):
    if index < 7:
        return index
    p2 = p3 = p5 = 0
    new_num = 1
    arr = []
    arr.append(new_num)
    while len(arr) < index:
        new_num = min(arr[p2] * 2, arr[p3] * 3, arr[p5] * 5)
        if arr[p2] * 2 == new_num:
            p2 += 1
        if arr[p3] * 3 == new_num:
            p3 += 1
        if arr[p5] * 5 == new_num:
            p5 += 1
        arr.append(new_num)
    return new_num

if __name__ == '__main__':
    index = 15
    print(get_ugly_num(index))