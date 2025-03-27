# Define a custom exception InvalidAgeError.
class InvalidAgeError(Exception):
    def __init__(self,message,error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
    def __str__(self):
        return f"Error message :{self.message} , code : {self.error_code}"
def check_age(age):
    if age < 0:
        raise InvalidAgeError(f"Age cannot be negative {age}",400)
    else:
        print(" Your age is",age)

try:
    check_age(12)
    check_age(0)
    check_age(-44)
except InvalidAgeError as e:
    print(e)
