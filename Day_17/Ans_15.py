# Use @staticmethod to define a utility function.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(MathUtils.add(10, 20))    # Output: 30
print(MathUtils.is_even(10))    # Output: True
print(MathUtils.is_even(7))     # Output: False
