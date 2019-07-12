# 面试题27：二叉树的镜像

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

# 镜像二叉树
def mirror_recursively(node):
    if not node:
        return
    tmp_node = node.left
    node.left = mirror_recursively(node.right)
    node.right = mirror_recursively(tmp_node)
    return node

if __name__ == '__main__':
    pre_traversal = [8, 6, 5, 7, 10, 9, 11]
    mid_traversal = [5, 6, 7, 8, 9, 10, 11]
    root = reconstruct_binary_tree(pre_traversal, mid_traversal)
    new_root = mirror_recursively(root)
    pass