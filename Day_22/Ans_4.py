# Convert an infix expression to postfix using a stack.
class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)>0:
            popped =self.stack.pop()
            return popped
        else:
            return False
    
        