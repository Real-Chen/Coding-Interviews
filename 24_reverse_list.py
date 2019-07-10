#面试题24：反转链表

# 定义节点结构
class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

# 通过数据生成链表
def list2linked_list(values):
    # 函数列表转链表
    # 输入列表值，输出链表头
    if not values:
        return None
    head = ListNode(values[0])
    before_node = head
    for num in values[1:]:
        node = ListNode(num)
        before_node.next = node
        before_node = node
    return head

# 打印链表
def print_list(head):
    if not head:
        return
    print(head.val,end='')
    node = head.next
    while node:
        print(f'->{node.val}',end='')
        node = node.next
    print()

# 循环实现反转链表
def reverse_list(head_node):
    if not head_node or not head_node.next:
        return head_node
    node1 = head_node
    node2 = head_node.next
    node3 = node2.next
    head_node.next = None
    while node3:
        node2.next = node1
        node1 = node2
        node2  = node3
        node3 = node3.next
    node2.next = node1
    return node2

# 递归实现反转连边， 代码更简洁，但是效率不高
def reverse_list_recursive(node):
    if not node or not node.next:
        return node, node
    new_head, tail = reverse_list_recursive(node.next)
    node.next = None
    tail.next = node
    return new_head, node


if __name__ == '__main__':
    # 循环实现
    vals = ['a', 'b']
    head = list2linked_list(vals)
    print_list(head)
    reverse_head = reverse_list(head)
    print_list(reverse_head)

    # 递归实现
    vals = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    head = list2linked_list(vals)
    print_list(head)
    reverse_head_recursive, _ = reverse_list_recursive(head)
    print_list(reverse_head_recursive)