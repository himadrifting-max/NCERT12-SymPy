import sympy as sp 
import numpy as np


# Question number 10 
# We have to find x, y, z and t equation is given

x, y, z, t = sp.symbols('x y z t')


# We are taking A as LHS:

A = 2*sp.Matrix([[x, z], [y, t]]) + 3*sp.Matrix([[1, -1], [0, 2]]) 

# B is actually the RHS of the same equation:

B = 3*sp.Matrix([[3, 5], [4, 6]])

# We simplified the equation of A (LHS)

Simple_A = sp.simplify(A)

print(Simple_A)


# we will now compare the corresponding elements

eq1 = sp.Eq(2*x + 3, 9)

eq2 = sp.Eq(2*y, 12)

eq3 = sp.Eq(2*z - 3, 15)

eq4 = sp.Eq(2*t + 6, 18)

# we are almost done with, now we have to solve it

solution = sp.solve([eq1, eq2, eq3, eq4], [x, y, z, t])

print(solution)





