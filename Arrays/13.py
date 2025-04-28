# Insert an element at a specific position
arr = [1,2,3,4,5,6,7,8,9]
def insert_at_positon(x,num,position):
    if position > len(x):
        return ("insert position of out range")
    x[position]= num
    return x
print("original list :",arr)
print("modified list : ",insert_at_positon(arr,44,4))