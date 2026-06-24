import sympy as sp
import numpy as np


#Question 1
A = sp.Matrix([[2, 4], [3, 2]])
B = sp.Matrix([[1, 3], [-2, 5]])
C = sp.Matrix([[-2, 5], [3, 4]])

# i) A + B
print("A + B =", A + B)

# ii) A - B
print("A - B =", A - B)

# iii) 3A - C
print("3A - C =", 3 * A - C)

# iv) AB
print("AB =", A * B)

#v) BA
print("BA =", B * A)