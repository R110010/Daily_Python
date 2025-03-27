# Implement nested try-except blocks.

def nested():
    try:
        print(" outer block")
        try:
            print("middle block")
            num1 = int(input(" enter a number :"))
            num2 = int(input(" Enter second number :"))
            result = num1/num2
            print("result :",result)
            try:
                print("inner block ")
                number = [1,2,3,4]
                ind = (int(input(" enter the index to be searched :")))
                data = number.index(ind)
                print(f"number at index {ind} is {data}")
            except IndexError:
                print(" inner block error")
        except ZeroDivisionError:
            print(" middle block error")
    except ValueError:
        print(" outer block error")
    finally:
        print(" execution completed")

nested()