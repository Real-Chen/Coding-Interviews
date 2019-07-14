# 面试题34：二叉树中和为某一值的路径

import copy
# 二叉树数据结构
class BinaryTreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# 递归重建二叉树
def reconstruct_binary_tree(pre_traversal, mid_traversal):
    if not pre_traversal or not mid_traversal:
        return None
    else:
        father_value = pre_traversal[0]
        index = mid_traversal.index(father_value)
        node = BinaryTreeNode(father_value)
        node.left = reconstruct_binary_tree(pre_traversal[1:index+1], mid_traversal[:index])
        node.right = reconstruct_binary_tree(pre_traversal[index+1:], mid_traversal[index+1:])
        return node

# 寻找路径
def find_path(root, expect_number):
    if not root or not expect_number:
        return []
    return find_path_core(root, 0, [], expect_number, [])

def find_path_core(node, count, path, expect_number, result):
    path.append(node.val)
    count += node.val
    if not node.left and not node.right:
        if count == expect_number:
            result.append(copy.deepcopy(path))
        path.pop(-1)
        count -= node.val
        return result

    if node.left:
        result = find_path_core(node.left, count, path, expect_number, result)
    if node.right:
        result = find_path_core(node.right, count, path, expect_number, result)
    path.pop(-1)
    count -= node.val
    return result

if __name__ == '__main__':
    pre_traversal = [1,2,4,5,3,6,7]
    mid_traversal = [4,2,5,1,6,3,7]
    root = reconstruct_binary_tree(pre_traversal, mid_traversal)
    target = 8
    result = find_path(root, target)
    print(result)