import sympy as sp
import numpy as np 

from sympy import Rational

# Question 1 
# Find the transpose of each of the following matrices
# i)
A = sp.Matrix([[5], [sp.Rational(1, 2)], [-1]])


A_T = sp.transpose(A)

print("Transpose of A =", A_T )


# ii) 

B = sp.Matrix([[1, 2], [2, 3]])

B_T = sp.transpose(B)

print("Transpose of B =", B_T )


# iii)

C = sp.Matrix([[-1, 5, 6], [sp.sqrt(3), 5, 6], [2, 3, -1]])

C_T = sp.transpose(C)

print("Transpose of C =", C_T )





