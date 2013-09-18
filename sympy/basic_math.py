# only works with Python 2
from sympy import Symbol, solve

# basic math
x = Symbol('x')
y = Symbol('y')
print(x+2*x+y+3*y)

# simple solving
print(solve(x**2 + 2*x + 1))
