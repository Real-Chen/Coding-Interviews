# 面试题31：栈的压入、弹出序列

def is_pop_order(push_nums, pop_nums):
    if not push_nums or not pop_nums:
        return False
    stack = []
    stack.append(push_nums.pop(0))
    while pop_nums:
        if not stack:
            stack.append(push_nums.pop(0))
        if pop_nums[0] == stack[-1]:
            pop_nums.pop(0)
            stack.pop(-1)
        elif push_nums:
            stack.append(push_nums.pop(0))
        else:
            return False
    return True

if __name__ == '__main__':
    print(is_pop_order([1,2,3,4,5], [3,4,5,1,2]))