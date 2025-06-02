# Check for balanced parentheses using a stack.
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0
    
def check_bal(expression):
    stack = Stack()
    opening = "{(["
    closing = "})]"
    match = {"}":"{", ")":"(", "]":"["}
    for exp in expression:
        if exp in opening:
            stack.push(exp)
        elif exp in closing:
            if stack.is_empty():
                return False
            else:
                last = stack.pop()
                if match[exp]!=last:
                    return False
    return True if stack.is_empty() else False
print(check_bal("{(())}"))