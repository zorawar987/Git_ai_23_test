import pytest
from calculator import Calculator, PreciseCalculator

# Calculator Fixture
@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (1, 0, "Cannot divide by zero")
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),
    (10, -1, 0.1)
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),       # 0! = 1
    (1, 1),       # 1! = 1
    (5, 120),     # 5! = 120
    (7, 5040),    # 7! = 5040
])
def test_factorial(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 0),       # Fibonacci(0) = 0
    (1, 1),       # Fibonacci(1) = 1
    (5, 5),       # Fibonacci(5) = 5
    (7, 13),      # Fibonacci(7) = 13
])
def test_fibonacci(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

# Testing precision with PreciseCalculator
@pytest.mark.parametrize("a, b, expected", [
    (1.235, 2.345, 3.58),  # rounded to 2 decimal places
    (3.142, 2.718, 5.86),  # rounded to 2 decimal places
])
def test_add_precision(calculator, a, b, expected):
    calc = PreciseCalculator(2)  # Use 2 decimal places
    assert calc.add(a, b) == expected
