# Handle ZeroDivisionError in a division function.
def division(num1,num2):
    try:
        result =num1/num2
        return result
    except Exception as e:
        return e
div = division(4,2)
print(div)
div2 = division(2,0)
print(div2)
