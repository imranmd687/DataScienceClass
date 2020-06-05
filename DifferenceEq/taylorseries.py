import sympy as sym
from sympy import Subs, Function
import numpy as np
import math

x = sym.Symbol('x')


def find_value_of_equation(expr, value):
    substitutedValue = expr.subs(x, 1)
    return substitutedValue


def find_taylor_Expansion(equation, value):
    f0 = expr.subs(x, 0)
    print(f0)
    sum = f0
    valueat = expr.subs(x, value)
    i = 1
    while sum != valueat:
        equation = sym.diff(equation, x)
        newterm = (equation.subs(x, 0)) / math.factorial(i)
        print(newterm)
        i += 1
        sum += newterm


if __name__ == "__main__":
    expr = 3 * x ** 3 + x ** 2 - 8 * x + 6
    find_value_of_equation(expr, 1)
    find_taylor_Expansion(expr, 1)

