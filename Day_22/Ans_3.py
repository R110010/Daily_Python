# Reverse a string using a stack.
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

s = Stack()
lines = "alphabet"
for char in lines:
    s.push(char)
print(s)
rev_s =Stack()
while s.peek()!=None:
    popped = s.pop()
    rev_s.push(popped)

reversed = "" .join(rev_s.stack)
print(reversed)
