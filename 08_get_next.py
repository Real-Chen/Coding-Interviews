# 面试题8：二叉树的下一个节点

# 二叉树数据结构
class BinaryTreeNode():
    def __init__(self, value):
        self.val = value
        self.father = None
        self.left = None
        self.right = None

# 递归重建二叉树
def reconstruct_binary_tree(father_node, pre_traversal, mid_traversal):
    if not pre_traversal or not mid_traversal:
        return None
    else:
        node_value = pre_traversal[0]
        index = mid_traversal.index(node_value)
        node = BinaryTreeNode(node_value)
        node.father = father_node
        node.left = reconstruct_binary_tree(node, pre_traversal[1: index+1], mid_traversal[: index])
        node.right = reconstruct_binary_tree(node, pre_traversal[index+1: ], mid_traversal[index+1: ])
        return node

# 广度遍历寻找对应节点
def traversal_find(node, value):
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node.val == value:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

def get_next_node(node):
    if not node:
        return None
    next_node = None
    if node.right:
        tmp_node = node.right
        while tmp_node.left:
            tmp_node = tmp_node.left
        next_node = tmp_node
    elif node.father:
        current_node = node
        father_node = node.father
        while father_node and current_node == father_node.right:
            current_node = father_node
            father_node = current_node.father
        next_node = father_node

    return next_node

if __name__ == '__main__':
    # 根据面试题7的代码重建二叉树
    pre_traversal = ['a', 'b', 'd', 'e', 'h', 'i', 'c', 'f', 'g']
    mid_traversal = ['d', 'b', 'h', 'e', 'i', 'a', 'f', 'c', 'g']
    head = reconstruct_binary_tree(None, pre_traversal, mid_traversal)
    start_node = traversal_find(head, 'a')
    next_node = get_next_node(start_node)
    if next_node:
        print(next_node.val)
    else:
        print(None)