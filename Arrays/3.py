# using Binary search find square root of a number.

def square_root(num):
    if num==0 or num==1:
        return num
    left, right = 0, num
    epsilon = 1e-6
    while (right-left)>epsilon:
        mid = (left + right)/2
        if mid*mid <num:
            left = mid
        else:
            right = mid
    return (left + right) /2
res = square_root(25)
print(res)