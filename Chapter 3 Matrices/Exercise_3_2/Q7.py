import sympy as sp
import numpy as np 

# Question number 7
# We have to find X and Y from a Matrix equation solution
# i) 

A = sp.Matrix([[7, 0], [2, 5]])

B = sp.Matrix([[3, 0], [0, 3]])
# Finding X

X = ( A + B )/ 2 

print("X =", X)

# Finding Y now

Y = A - X 

print("Y =", Y)

# ii)

C = sp.Matrix([[2, 3], [4,0]])

D = sp.Matrix([[2, -2], [-1,5]])

# Finding Y but here we are taking it as J

J = (3*C - 2*D) / 5

print("Y =", J)

# We are finding X now but it is called I now 

I = (C - 3*J) / 2

print("X =", I)