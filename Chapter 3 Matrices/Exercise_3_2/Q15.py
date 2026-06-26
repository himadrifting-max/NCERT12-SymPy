import sympy as sp
import numpy as np


# Question 15
# We have to find the equation from the matrix A 

A = sp.Matrix([[2, 0, 1], [2, 1, 3], [1, -1, 0]])

# The equation we have to find out is A**2 - 5*A + 6I =
# The equations has an "I" which is an identity matrix

I = sp.eye(3)

# print(I)

# Let 6*I known as D

D = 6*I

# print(D)

# Let A**2 be B

B = A**2

# print(B)


# We are once again letting 5A as C 

C = 5*A

# print(C)

# Now we will form the equation A**2 - 5A + 6I which will be known as E

E = (B) - (C) + (D)

print(E)
