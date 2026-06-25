import sympy as sp

import numpy as np 

# Question 4 

# We  have to compute ( A + B ) and ( B - C ). Then have to verify A + ( B - c ) =  ( A + B ) - C 
 
A = sp.Matrix([[1, 2, -3], [5, 0, 2], [1, -1, 1]])

B = sp.Matrix([[3, -1, 2], [4, 2, 5], [2, 0, 3]])

C = sp.Matrix([[4, 1, 2], [0, 3, 2], [1, -2, 3]])

# Computing ( A + B )

print( "A + B =", A + B )

# Computing ( B - C )

print("B - C =", B - C )

# LHS :
 
LHS = print( "A + ( B - c ) =", A + ( B - C ) )

# RHS :

RHS = print("( A + B ) - C = ", ( A + B ) - C  )

if LHS == RHS:
    print("Verified: A + ( B - C ) = ( A + B ) - C")
else:
    print("Not Verified")
       