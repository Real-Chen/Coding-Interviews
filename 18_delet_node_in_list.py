# 面试题18：删除链表的节点
def delet_node_in_list(head, node):


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


if __name__ == '__main__':
    values = ['a', 'b', 'c', 'e', 'f', 'g', 'h']
    head, node = list2linked_list(values, 'b')