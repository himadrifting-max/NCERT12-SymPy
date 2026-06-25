import sympy as sp
import numpy as np


# Question number 11
# We have to find x and y the equation is given

x , y = sp.symbols('x y')

# We are taking A as LHS:

A = x*sp.Matrix([2,3]) + y*sp.Matrix([-1, 1])

# B is actually the RHS of the same equation:

B = sp.Matrix([10, 5])


# We simplified the equation of A (LHS)

Simple_A = sp.simplify(A)

print(Simple_A)




# we will now compare the corresponding elements

eq1 = sp.Eq(2*x - y, 10)

eq2 = sp.Eq(3*x + y, 5)



# we are almost done with, now we have to solve it

solution = sp.solve([eq1, eq2], [x, y])

print(solution)




