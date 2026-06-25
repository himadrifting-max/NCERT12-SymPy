import sympy as sp
import numpy as np

# Question 14
# We have to prove two questions that they are not equals to 
# i)

# first lets simplify the LHS:

A = sp.Matrix([[5, -1], [6, 7]]) * sp.Matrix([[2, 1], [3, 4]])

sp.simplify(A)

print("LHS =", A)

LHS = A

# We got the LHS now its time to do the same with RHS

B = sp.Matrix([[2, 1], [3, 4]]) * sp.Matrix([[5, -1], [6, 7]])

sp.simplify(B)

print(("RHS =") , B)

RHS = B

# now we have to show LHS isnt equal to RHS:

if LHS != RHS:
    print("Verified: LHS ≠ RHS")
else: 
    print("Not Verified")


# ii) we have proved the first part lets solve the second part 

# first lets simplify the LHS:

A = sp.Matrix([[1, 2, 3], [0, 1, 0], [1, 1, 0]]) * sp.Matrix([[-1, 1, 0], [0, -1, 1], [1, 1, 0]])

sp.simplify(A)

print("LHS =", A)

LHS = A


# We got the LHS now its time to do the same with RHS

B = sp.Matrix([[-1, 1, 0], [0, -1, 1], [2, 3, 4]]) * sp.Matrix([[1, 2, 3], [0, -1, 0], [1, 1, 0] ])

sp.simplify(B)

print(("RHS =") , B)

RHS = B



# now we have to show LHS isnt equal to RHS:

if LHS != RHS:
    print("Verified: LHS ≠ RHS")
else: 
    print("Not Verified")


