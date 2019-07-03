class queue_by_stack():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, value):
        self.stack1.append(value)

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