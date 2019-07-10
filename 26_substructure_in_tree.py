# 面试题26：树的子结构

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

# 判断两端是否为子树
def has_subtree(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.val == root2.val and does_tree1_has_tree2(root1.left, root2.left) and does_tree1_has_tree2(root1.right, root2.right):
        return True
    else:
        return has_subtree(root1.left, root2) or has_subtree(root1.right, root2)

# 判断树1是否包含树2
def does_tree1_has_tree2(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.val == root2.val:
        return does_tree1_has_tree2(root1.left, root2.left) and does_tree1_has_tree2(root1.right, root2.right)
    else:
        return False

if __name__ == '__main__':
    pre_traversal_1 = [1, 8, 9, 2, 4, 7, 7]
    mid_traversal_1 = [9, 8, 4, 2, 7, 1, 7]
    root1 = reconstruct_binary_tree(pre_traversal_1, mid_traversal_1)

    pre_traversal_2 = [8, 9, 2]
    mid_traversal_2 = [9, 8, 2]
    root2 = reconstruct_binary_tree(pre_traversal_2, mid_traversal_2)
    # pos_traversal(head)
    print(has_subtree(root1, root2))