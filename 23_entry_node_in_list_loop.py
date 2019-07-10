# 面试题23：链表中环的入口节点

# 定义链表结构
class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

# 生成带环链表
def list2linked_list(values, pos):
    # 函数列表转链表
    # 输入列表值,以及想要删除的节点值，输出链表头，和该节点
    if not values:
        return None
    head = ListNode(values[0])
    before_node = head
    node = head
    for num in values[1:]:
        node = ListNode(num)
        before_node.next = node
        before_node = node

    if pos >= len(values) or pos < 0:
        pass
    else:
        current_node = head
        for _ in range(pos):
            current_node = current_node.next
        node.next = current_node
    return head

# 寻找环入口
# 这里并没有采用剑指offer上的实现方式，而是采用了leetcode上的实现方式，少了一步求环大小的步骤，计算量更小
# 具体原理可参考英文版leetcode该题的讨论版
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything
# 具体证明参考三哥的原理解析视频
# https://www.youtube.com/watch?time_continue=2&v=zbozWoMgKW0
def entry_node_of_loop(head):
    if not head or not head.next:
        return head
    p1 = head.next
    p2 = head.next.next
    while p1 != p2 and p1 and p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    if_loop = (p1 == p2)
    if if_loop:
        p2 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    else:
        return None


if __name__ == '__main__':
    values = [3, 2, 0, -4]
    pos = 3
    head = list2linked_list(values, pos)
    print(entry_node_of_loop(head).val)