# Check for balanced parentheses using a stack.
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
def check_balanced_paranthesis(expression):
    opening = "[{("
    closing = "]})"
    match={"}":"{","]":"[",")":"("}
    stack =Stack()
    for exp in expression:
        if exp in opening:
            stack.push(exp)
        elif exp in closing:
            if stack.is_empty():
                return False
            else:
                popped = stack.pop()
                if match[exp]!=popped:
                    return False
        return True
    
res = check_balanced_paranthesis("{()}")
print(res)