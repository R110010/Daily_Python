# Implement a function that logs errors to a file.
def log_error(error):
    with open("error_log.txt","a") as file:
        file.write(str(error)+"\n")
def division(a,b):
    try:
        result = a/b
        print(result)
    except (ZeroDivisionError,ValueError,TypeError) as e:
        log_error(e)
        print(e)
division(12,4)
division(2,0)
division("f",2)
division(44,"y")
