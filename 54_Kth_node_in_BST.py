# 面试题54：二叉搜索树的第k大节点

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

def Kth_node(root, k):
    if not root or k == 0:
        return None
    target, k = Kth_node_core(root, k)
    return target

def Kth_node_core(root, k):
    target = None
    if root.left:
        target, k = Kth_node_core(root.left, k)
    if target == None:
        if k == 1:
            target = root
        k -= 1
    if target == None and root.right != None:
        target, k = Kth_node_core(root.right, k)
    return target, k

if __name__ == '__main__':
    pre = [5,3,2,4,7,6,8]
    mid = [2,3,4,5,6,7,8]
    root = reconstruct_binary_tree(pre, mid)
    k = 3
    print(Kth_node(root, k).val)
