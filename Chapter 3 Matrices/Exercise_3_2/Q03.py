import sympy as sp
import numpy as np

# Question 3
# Compute the indicated products
# i)
a, b = sp.Symbol('a'), sp.Symbol('b')

A = sp.Matrix([[a, b], [-b, a]])

B = sp.Matrix([[a, -b], [b, a]])

print("AB =", A * B)

# ii)
C = sp.Matrix([[1], [2], [3]])

D = sp.Matrix([[2,3,4]])

print("CD =", C * D)

# iii)
I = sp.Matrix([[1, -2], [2, 3]])
J = sp.Matrix([[1, 2, 3], [2, 3, 1]])

print("IJ =", I * J)

# iv)
M = sp.Matrix([[2, 3, 4], [3, 4, 5], [4, 5, 6]]) 
N = sp.Matrix([[1, -3, 5], [0, 2, 4], [3, 0, 5]]) 

print("MN =", M * N) 

# v)
P = sp.Matrix([[2, 1], [3,2], [-1,1]])
Q = sp.Matrix([[1, 0 , 1], [-1, 2, 1]]) 

print("PQ =", P * Q)

# vi)
X = sp.Matrix([[3, -1, 3],  [-1, 0, 2]]) 
Y = sp.Matrix([[2,-3], [1,0], [3,1]]) 

print("XY =", X * Y)

