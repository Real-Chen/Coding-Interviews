# 面试题18：删除链表的节点
def delet_node_in_list(head, node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next
        return
    elif not head.next:
        return None
    else:
        current_node = head
        while current_node.next != node:
            current_node = current_node.next
        current_node.next = node.next
        del node
    return

# 使用面试题6中创建链表的方法创建
class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

def list2linked_list(values, target_value):
    # 函数列表转链表
    # 输入列表值,以及想要删除的节点值，输出链表头，和该节点
    if not values:
        return None
    head = ListNode(values[0])
    before_node = head
    target_node = None
    for num in values[1:]:
        node = ListNode(num)
        before_node.next = node
        before_node = node
        if num == target_value:
            target_node = node
    return head, target_node

# 打印链表
def print_list(head):
    print(head.val,end='')
    node = head.next
    while node:
        print(f'->{node.val}',end='')
        node = node.next


if __name__ == '__main__':
    values = ['a', 'b', 'c', 'e', 'f', 'g', 'h']
    head, node = list2linked_list(values, 'a')
    delet_node_in_list(head, node)
    print_list(head)