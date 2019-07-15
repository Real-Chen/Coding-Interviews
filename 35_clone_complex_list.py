# 面试题35：复杂链表的复制
class RandomListNode():
    def __init__(self, val):
        self.label = val
        self.next = None
        self.random = None

def init_example():
    A = RandomListNode('A')
    B = RandomListNode('B')
    C = RandomListNode('C')
    D = RandomListNode('D')
    E = RandomListNode('E')
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    A.random = C
    B.random = E
    D.random = B
    return A

# 根据哈希表复制链表
def clone_nodes_hash(head):
    new_head = RandomListNode(head.label)
    before_node = new_head
    node = head.next
    node_map = {head: new_head}
    while node:
        new_node = RandomListNode(node.label)
        before_node.next = new_node
        node_map[node] = new_node
        before_node = new_node
        node = node.next
    node = head
    while node:
        if node.random:
            node_map[node].random = node_map[node.random]
        node = node.next
    return new_head


def clone_nodes(pHead):
    if not pHead:
        return
    if not pHead.next:
        return RandomListNode(pHead.label)
    # 第一步：顺序复制链表
    node = pHead
    while node:
        new_node = RandomListNode(node.label)
        new_node.next = node.next
        node.next = new_node
        node = new_node.next
    # 第二步：复制跳转关系
    node = pHead
    while node:
        if node.random:
            node.next.random = node.random.next
        node = node.next.next
    # 第三步：根据奇偶拆分链表
    new_head = pHead.next
    node = pHead
    while node:
        copy_node = node.next
        node.next = copy_node.next
        if node.next:
            copy_node.next = node.next.next
        node = node.next
    return new_head


if __name__ == '__main__':
    head = init_example()
    copy_head = clone_nodes(head)
    pass