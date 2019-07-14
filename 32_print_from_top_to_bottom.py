# 面试题32：从上往下打印二叉树

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

# 从上往下打印二叉树
def print_from_top_to_bottom(root):
    if not root:
        return []
    queue = [root]
    values = []
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        values.append(node.val)
    return values

if __name__ == '__main__':
    pre_traversal = [1,2,4,7,8,3,5,6]
    mid_traversal = [7,4,8,2,1,5,3,6]
    root = reconstruct_binary_tree(pre_traversal, mid_traversal)
    print(print_from_top_to_bottom(root))