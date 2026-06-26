import sympy as sp
import numpy as np


# Question 16
# We have to prove an equation is equals to 0

A = sp.Matrix([[1, 0, 2], [0, 2, 1], [2, 0, 3]])

# Let A**2 be B

B = A**3

# print(B)

# Let 6A**2 be C

C = 6*A**2

# print(C)

# We have to assign I as Identity Matrix

I = sp.eye(3)


# Let 7*A known as D

D = 7*A

# print(D)

# Let 2*I known as E

E = 2*I

# print(E)


# Now we are almost done, we just have to form the equation now and I am assigning the equation as (X)

X = (B) - (C) + (D) + (E)

print(X)


# Now we have to prove the equation is equals to 0 

if X == sp.zeros(3):
    print("Hence, proved")
else:
    print("Not proved")