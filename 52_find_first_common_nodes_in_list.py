# 面试题52：两个链表的第一个公共节点

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def construct_list(nums_1, nums_2, common_val):
    if not nums_1 or not nums_2:
        return None
    head_1 = ListNode(nums_1[0])
    before_node = head_1
    for num in nums_1[1:]:
        node = ListNode(num)
        before_node.next = node
        before_node = node
        if num == common_val:
            common_node = node

    head_2 = ListNode(nums_2[0])
    before_node = head_2
    for num in nums_2[1:]:
        node = ListNode(num)
        before_node.next = node
        before_node = node
    node.next = common_node
    return head_1, head_2

def find_first_common_node(head1, head2):
    if not head1 or not head2:
        return None
    node = head1
    length_1 = 0
    while node:
        length_1 += 1
        node = node.next
    node = head2
    length_2 = 0
    while node:
        length_2 += 1
        node = node.next

    long_node = head1
    short_node = head2
    length_diff = abs(length_1 - length_2)
    if length_1 < length_2:
        long_node = head2
        short_node = head1
    for _ in range(length_diff):
        long_node = long_node.next

    while long_node and short_node and (long_node != short_node):
        long_node = long_node.next
        short_node = short_node.next
    return long_node



if __name__ == '__main__':
    list_1 = [1,2,3,6,7]
    list_2 = [4,5]
    head1, head2 = construct_list(list_1, list_2, 6)
    print(find_first_common_node(head1, head2).val)