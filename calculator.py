# Calculator class definition
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    
    def power(self, a, b):
        if b < 0:
            return 1 / (a ** abs(b))  # Correct handling of negative exponents
        return a ** b
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        return n if n <= 1 else self.fibonacci(n - 1) + self.fibonacci(n - 2)


# PreciseCalculator class definition (extends Calculator)
class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result
