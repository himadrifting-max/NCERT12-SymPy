#NCERT Class 12 Mathematics Exercise 3.1 Question 1



import numpy as np 
import sympy as sp
from sympy import symbols, Matrix, Rational, sqrt


x = sp.symbols('x')
#Question 1 

A = sp.Matrix([[2, 5, 19, -7],
               [35, -2, sp.Rational(5,2), 12], 
               [sp.sqrt(3), 1 , -5, 17]
                ])

#i) The order of the matrix A
print("The order of the matrix A is:", A.shape)

#ii) The number of elements in the matrix A
num_elements = A.shape[0] * A.shape[1]
print("The number of elements in the matrix A is:", num_elements)

#iii) Write the elements a13, a21, a33, a24, a23. 
print("a13 =" , A[0, 2])
print("a21 =" , A[1, 0])
print("a33 =" , A[2, 2])
print("a24 =" , A[1, 3])
print("a23 =" , A[1, 2])

# Answer:
# The order of the matrix A is: (3, 4)
# The number of elements in the matrix A is: 12
# a13 = 19
# a21 = 35
# a33 = -5
# a24 = 12
# a23 = 5/2