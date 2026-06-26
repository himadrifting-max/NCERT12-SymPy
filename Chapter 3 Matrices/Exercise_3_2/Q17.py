import sympy as sp
import numpy as np

# Question 17
# We have to find k in this equation A**2 = kA - 2I

k = sp.Symbol('k')

# The given values are

A = sp.Matrix([[3, -2], [4, -2]])

I = sp.eye(2)

# We are letting A**2 as B

B = A**2

# print(B)

# then we are letting k*A as C

C = k*A

# print(C)

# RHS = kA - 2I

RHS  = C - 2*I 

# So the LHS will be:

print("A**2 =", B )

# So the RHS will be:

print("kA - 2I", RHS)


# Now we just have to form equations and then solve them

eq1 = sp.Eq(B[0,0], RHS[0, 0])
eq2 = sp.Eq(B[0,1], RHS[0, 1])
eq3 = sp.Eq(B[1,0], RHS[1, 0])
eq4 = sp.Eq(B[1,1], RHS[1, 1])

print(eq1)
print(eq2)
print(eq3)
print(eq4)


# now we just have to solve it

solution = sp.solve([eq1, eq2, eq3, eq4], k)
print(solution)







