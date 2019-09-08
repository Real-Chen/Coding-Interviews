# 面试题55-1：二叉树的深度

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

def tree_depth(node):
    if not node:
        return 0
    left = tree_depth(node.left)
    right = tree_depth(node.right)
    return max(left, right) + 1

if __name__ == '__main__':
    pre = [1,2,4,5,7,3,6]
    mid = [4,2,7,5,1,3,6]
    root = reconstruct_binary_tree(pre, mid)
    print(tree_depth(root))