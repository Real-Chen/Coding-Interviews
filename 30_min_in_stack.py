# 面试题30：包含min函数的栈

class stack_min():
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, val):
        self.data_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.data_stack.pop()

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

if __name__ == '__main__':
    stack = stack_min()
    stack.push(3)
    print(stack.min())
    stack.push(4)
    print(stack.min())
    stack.push(2)
    print(stack.min())
    stack.push(1)
    print(stack.min())
    print(stack.pop())
    print(stack.pop())
    stack.push(0)
    print(stack.min())