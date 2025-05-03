class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,item):
        self.stack.append(item)
    def is_empty(self):
        if len(self.stack)==0:
            return True
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            None
    def __str__(self):
        return str(self.stack)
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
print(s.peek())
print("popped item :",s.pop())
print(s)