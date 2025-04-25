# Sort a stack using another stack.
def sort_stack(input_stack):
    temp_stack= list()
    while input_stack:
        temp = input_stack.pop()
        while temp_stack and temp_stack[-1] >temp:
            input_stack.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack

stack = [2,8,3,5,14,7]
print(stack)
sorted = sort_stack(stack)
print(sorted)