# Implement a stack using a list with push and pop operations.
class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            popped =self.stack.pop()
            return popped
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
s =Stack()
s.push(20)
s.push(40)
s.push(60)
print(s)
print(s.peek())
print(s.pop())
print(s)