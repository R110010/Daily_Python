# reverse a string using stack.
class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,item):
        self.stack.append(item)
    def is_empty(self):
        return len(self.stack)==0
    def pop(self):
        return self.stack.pop()
    def __str__(self):
        return str(self.stack)
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
def reverse_string(line):
    s=Stack()
    for char in line:
        s.push(char)
    r=Stack()
    while s.peek():
        popped = s.pop()
        r.push(popped)
    reversed_stack = "".join(r.stack)
    print(reversed_stack)

reverse_string("abcdefghijklmnopqrstuvwxyz")