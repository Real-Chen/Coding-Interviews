# 面试题33：二叉搜索树的后序遍历

def verify_sequence(input_tranversal):
    if not input_tranversal:
        return False
    else:
        return verify_sequence_core(input_tranversal)

def verify_sequence_core(input_tranversal):
    if len(input_tranversal) <= 1:
        return True
    root = input_tranversal[-1]
    split_point = 0
    while split_point < len(input_tranversal) and input_tranversal[split_point] < root:
        split_point += 1
    for i in range(split_point, len(input_tranversal)-1):
        if input_tranversal[i] < root:
            return False
    return verify_sequence_core(input_tranversal[:split_point]) and verify_sequence_core(input_tranversal[split_point:-1])


if __name__ == '__main__':
    post_tranversal = [1,3,2,4,7,6,9,8,5]
    print(verify_sequence(post_tranversal))

    post_tranversal = [9,3,2,4,7,6,1,8,5]
    print(verify_sequence(post_tranversal))