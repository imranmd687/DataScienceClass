from random import randint
import sympy as sym
import numpy as np

x, y = sym.symbols('x y')


def find_gradient(str):
    val = str.split("=")
    print(val[1])
    grad_x = sym.diff(val[1], x)
    grad_y = sym.diff(val[1], y)
    grad_vector = [grad_x, grad_y]
    resultList = []
    for _ in range(0,10):
        resultList.append([grad_x.subs(x, randint(0, 10)), grad_y.subs(y, grad_y.subs(y, randint(0, 10)))])
    return resultList


if __name__ == "__main__":
    print(find_gradient("f(z)=x**2+y**2"))
