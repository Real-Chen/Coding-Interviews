# 面试题9： 用两个栈实现队列

# 新建队列类，内部用栈实现
class queue_by_stack():
    def __init__(self):
        # python的栈和队列都是用列表实现的
        # 这里用列表表示栈，规定只能用pop()的操作
        self.stack1 = []
        self.stack2 = []

    # 队尾加值
    def append_tail(self, value):
        self.stack1.append(value)

    # 弹出队首的数据
    def pop_head(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == '__main__':
    queue = queue_by_stack()
    queue.append_tail('a')
    print(queue.pop_head())
    queue.append_tail('b')
    queue.append_tail('c')
    print(queue.pop_head())
    queue.append_tail('d')
    queue.append_tail('e')
    queue.append_tail('f')
    print(queue.pop_head())
    print(queue.pop_head())
    print(queue.pop_head())
    print(queue.pop_head())