# 面试题25：合并两个排序的链表

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

# 合并链表 常规写法
def merge(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    # 找到链表头
    if head1.val <= head2.val:
        head = head1
        node1 = head1.next
        node2 = head2
    else:
        head = head2
        node1 = head1
        node2 = head2.next

    tail = head
    while node1 or node2:
        if not node1:
            tail.next = node2
            tail = node2
            node2 = node2.next
        elif not node2:
            tail.next = node1
            tail = node1
            node1 = node1.next
        elif node1.val <= node2.val:
            tail.next = node1
            tail = node1
            node1 = node1.next
        else:
            tail.next = node2
            tail = node2
            node2 = node2.next
    return head

# 递归解法
def merge_recursive(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        head1.next = merge_recursive(head1.next, head2)
        return head1
    else:
        head2.next = merge_recursive(head1, head2.next)
        return head2


if __name__ == '__main__':
    # 递归实现
    val1 = [1, 3, 5, 7]
    val2 = [2, 4, 6, 8]
    list_head1 = list2linked_list(val1)
    list_head2 = list2linked_list(val2)
    print_list(list_head1)
    print_list(list_head2)
    merge_head = merge_recursive(list_head1, list_head2)
    print_list(merge_head)

    # 非递归实现
    val1 = [1, 3, 5, 7]
    val2 = [2, 4, 6, 8]
    list_head1 = list2linked_list(val1)
    list_head2 = list2linked_list(val2)
    print_list(list_head1)
    print_list(list_head2)
    merge_head = merge(list_head1, list_head2)
    print_list(merge_head)