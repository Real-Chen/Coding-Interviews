# 面试题28：对称二叉树

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

# 判断是否镜像
def is_symmetrical_tree(root):
    return is_symmetrical(root, root)

def is_symmetrical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return is_symmetrical(root1.left, root2.right) and is_symmetrical(root1.right, root2.left)

if __name__ == '__main__':
    pre_traversal = [8,6,5,7,6,7,5]
    mid_traversal = [5,6,7,8,7,6,5]
    root = reconstruct_binary_tree(pre_traversal, mid_traversal)
    print(is_symmetrical_tree(root))