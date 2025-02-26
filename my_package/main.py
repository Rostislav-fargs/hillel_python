"""#1"""

from string_utils import *
from math_utils import *

if __name__ == "__main__":
    print("Факторіал 6:", factorial(6))
    # print("Факторіал 2.5:", factorial(2.5))
    # print("Факторіал -3:", factorial(-3))
    print()
    print("НСД 112 і 32:", my_gcd(112, 32))
    print("НСД -96 і 6", my_gcd(-96, 6))
    # print("НСД 112 і 6.5", my_gcd(112, 6.5))
    # print("НСД 96 і '6'", my_gcd(96, "6"))
    print()
    print(f"Обрізання пробілів на кінцях рядка: _{cut_whitespace('     яблуко      ')}_")
    print(f"Обрізання пробілів на кінцях рядка: _{cut_whitespace(' 5   ябулко   -    ')}_")
    print(f"Обрізання пробілів на кінцях рядка: _{cut_whitespace('    ')}_")
    # print(f"Обрізання пробілів на кінцях рядка: _{cut_whitespace([6, '67' ,7])}_")
    print()
    print(f"Перетворення рядка на верхній регістр:", to_upper("нижній 12 регістр %"))
    print(f"Перетворення рядка на верхній регістр:", to_upper("Речення"))
    print(f"Перетворення рядка на верхній регістр:", to_upper("КАПС"))
    # print(f"Перетворення рядка на верхній регістр:", to_upper(8))
