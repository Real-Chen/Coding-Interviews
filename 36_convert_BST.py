# 面试题36：二叉搜索树和双向链表

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

def print_linkedList(root):
    print(f'{root.val}', end='')
    node = root.right
    while node:
        print(f'->{node.val}', end='')
        node = node.right
    print()

def convert_node(root):
    if not root or (not root.left and not root.right):
        return root
    head, tail = convert_node_core(root)
    return head

def convert_node_core(node):
    if node.left:
        head_l, tail_l = convert_node_core(node.left)
        tail_l.right = node
        node.left = tail_l
    else:
        head_l = node
    if node.right:
        head_r, tail_r = convert_node_core(node.right)
        head_r.left = node
        node.right = head_r
    else:
        tail_r = node
    return head_l, tail_r

if __name__ == '__main__':
    pre_traversal = [10,6,4,8,14,12,16]
    mid_traversal = [4,6,8,10,12,14,16]
    root = reconstruct_binary_tree(pre_traversal, mid_traversal)
    print_linkedList(root)
    head = convert_node(root)
    print_linkedList(head)

