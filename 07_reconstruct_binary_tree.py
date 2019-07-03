# 面试题7：重建二叉树

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

# 后序遍历
def pos_traversal(node):
    if not node:
        return
    pos_traversal(node.left)
    pos_traversal(node.right)
    print(node.val)
    return

if __name__ == '__main__':
    pre_traversal = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_traversal = [4, 7, 2, 1, 5, 3, 8, 6]
    head = reconstruct_binary_tree(pre_traversal, mid_traversal)
    pos_traversal(head)