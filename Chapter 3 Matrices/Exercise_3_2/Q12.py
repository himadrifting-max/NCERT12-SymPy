import sympy as sp 
import numpy as np


# Question number 12
# We have to find x, y, z and w equation is given

x, y, z, w = sp.symbols('x y z w')


# We are taking A as LHS:

A = 3*sp.Matrix([[x, y], [z, w]])

# B is actually the RHS of the same equation:

B = sp.Matrix([[x, 6], [-1, 2*w]]) + sp.Matrix([[4, x + y], [z + w, 3]])


# We simplified the equation of A (LHS)

Simple_A = sp.simplify(A)

print(Simple_A)



# We simplified the equation of B (RHS)

Simple_B = sp.simplify(B)

print(Simple_B)

# we will now compare the corresponding elements

eq1 = sp.Eq(3*x , x + 4)

eq2 = sp.Eq(3*y, 6 + x + y)

eq3 = sp.Eq(3*z, -1 + z + w)

eq4 = sp.Eq(3*w, 2*w + 3)



# we are almost done with, now we have to solve it

solution = sp.solve([eq1, eq2, eq3, eq4], [x, y, z, w])

print(solution)


