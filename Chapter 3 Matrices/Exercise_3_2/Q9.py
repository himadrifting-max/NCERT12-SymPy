import sympy as sp
import numpy as np

# Question number 9
# We have to find x and y equation is given
x , y = sp.symbols('x y')

# We are taking A as LHS:

A = 2*sp.Matrix([[1, 3], [0, x]]) + sp.Matrix([[y, 0], [1, 2]]) 

# B is actually the RHS of the same equation:

B = sp.Matrix([[5, 6], [1, 8]])

# We simplified the equation of A (LHS)

Simple_A = sp.simplify(A)

print(Simple_A)

# we will now compare the corresponding elements

eq1 = sp.Eq(y + 2, 5)

eq2 = sp.Eq(2*x + 2, 8)


# we are almost done with, now we have to solve it

solution = sp.solve([eq1, eq2], [x, y])

print(solution)