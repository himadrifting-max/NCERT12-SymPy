import sympy as sp 
import numpy as np 

# Question number 8
# We have to find X where an equation for Y is given

X = sp.symbols('X')

Y = sp.Matrix([[3, 2], [1, 4]])

# We are letting 2X + Y as Z

Z =sp.Matrix([[1, 0], [-3, 2]])

X = (Z - Y) / 2

print("X =", X)

