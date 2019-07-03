# 面试题6：从尾到头打印链表
# 两种实现：利用栈和利用递归

class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

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

def reverse_print_stack(head):
    # 用堆栈实现反向打印
    val_stack = []
    node = head
    # 压栈
    while node:
        val_stack.append(node.val)
        node = node.next
    # 打印
    while val_stack:
        print(val_stack.pop())

def reverse_print_recursively(node):
    # 递归实现反向打印
    if node.next:
        reverse_print_recursively(node.next)
    print(node.val)


if __name__ == '__main__':
    values = [0, 1, 2, 3, 4, 5]
    head = list2linked_list(values)
    reverse_print_stack(head)
    reverse_print_recursively(head)