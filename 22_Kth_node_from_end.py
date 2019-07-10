# 面试题22：链表中倒数第k个节点

# 定义链表结构
class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

# 生成链表
def list2linked_list(values):
    # 函数列表转链表
    # 输入列表值,以及想要删除的节点值，输出链表头，和该节点
    if not values:
        return None
    head = ListNode(values[0])
    before_node = head
    for num in values[1:]:
        node = ListNode(num)
        before_node.next = node
        before_node = node
    return head

def find_kth_to_tal(head, k):
    if not head or k <= 0:
        return None
    pre_node = head
    for _ in range(k):
        if pre_node:
            pre_node = pre_node.next
        else:
            return None
    behind_node = head
    while pre_node:
        behind_node = behind_node.next
        pre_node = pre_node.next
    return behind_node

if __name__ == '__main__':
    k = 4
    values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    head = list2linked_list(values)
    print(find_kth_to_tal(head, k).val)