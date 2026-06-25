import sympy as sp 
import numpy as np 

# Question 5
# we have to compute 3A - 5B

A = sp.Matrix([[sp.Rational(2, 3), 1, sp.Rational(5,3)], [sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(4, 3)], [sp.Rational(7, 3), 2, sp.Rational(2, 3)]])

B = sp.Matrix([[sp.Rational(2, 5), sp.Rational(3, 5), 1], [sp.Rational(1, 5), sp.Rational(2, 3), sp.Rational(4,3)], [sp.Rational(7, 5), sp.Rational(6, 5), sp.Rational(2, 5)]])

# 3A:

print("3A =", 3*A )

# 5B:

print("5B =", 5*B )

# 3A - 5B 

print("3A - 5B =", 3*A - 5*B)