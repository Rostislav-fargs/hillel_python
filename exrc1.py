"""Завдання #1"""

import math

class UnknownOperationError(Exception):
    """Class about error operator in math operation."""

    def __init__(self, operator, message):
        self.operator = operator
        self.message = f"{message} '{operator}'"
        super().__init__(self.message)

def calculate(a: int | float, b: int | float, operator: str):
    """Calculate values a and b with operator"""
    try:
        if (
            not isinstance(a, (int, float)) or
            not isinstance(a, (int, float)) or
            not isinstance(operator, str)
        ):
            raise TypeError(
                "'a' and 'b' must be float, integer or string, 'operanot' must be string"
            )

        if operator in '+-*/':
            result = eval(f"{a}{operator}{b}")
            if math.isinf(result):
                raise OverflowError()
        else:
            raise UnknownOperationError(operator, "operator must be in '+-/*', not")

    except ZeroDivisionError:
        print("Division by zero is impossible")
    except TypeError as e:
        print(f"Invalid type of arguments: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except UnknownOperationError as e:
        print(f"{e.__class__.__name__}: {e}")
    except OverflowError as e:
        print(e.__class__.__name__)

        while abs(a) > 1e154 or abs(b) > 1e154:
            a /= 10
            b /= 10
        print(f"Numbers were too large. Adjusting: a = {a}, b = {b}")
        return calculate(a, b, operator)

    else:
        print(f"{a} {operator} {b} = {result:.5f}")

    return None


if __name__ == "__main__":
    my_a = float(input("a: "))
    my_b = float(input("b: "))
    my_operator = input("operator: ")

    calculate(my_a, my_b, my_operator)
