import sympy as sp
import numpy as np
from sympy import symbols, Matrix, Rational, sqrt, sin, cos, tan, cot, sec, csc

# Question 2
# Compute the following:
# i) 
a, b = sp.symbols('a b')

A = Matrix([[a, b], [-b, a]])

B = Matrix([[a , b ] , [b, a]])

print( A + B )

#ii) 
a, b, c = sp.symbols('a b c')

X = Matrix([[a**2 + b**2, b**2 + c**2], [a**2 + c**2, a**2 + b**2]])

Y =Matrix([[2*a*b, 2*b*c], [-2*a*c, -2*a*b]])

print( X + Y )

# iii)
P = Matrix([[-1, 4, -6], [8, 5, 16], [2, 8, 5]])
Q = Matrix([[12, 7, 6], [8, 0, 5], [3, 2, 4]])

print( P + Q )

# iv)
x = sp.symbols('x')

I = Matrix([[cos(x)**2, sin(x)**2], [sin(x)**2, cos(x)**2]])
J = Matrix([[sin(x)**2, cos(x)**2], [cos(x)**2, sin(x)**2]])

print( I + J )

import sympy as sp
import numpy as np
from sympy import symbols, Matrix, Rational, sqrt, sin, cos, tan, cot, sec, csc

# Question 2
# Compute the following:
# i) 
a, b = sp.symbols('a b')

A = Matrix([[a, b], [-b, a]])

B = Matrix([[a , b ] , [b, a]])

print( A + B )

#ii) 
a, b, c = sp.symbols('a b c')

X = Matrix([[a**2 + b**2, b**2 + c**2], [a**2 + c**2, a**2 + b**2]])

Y =Matrix([[2*a*b, 2*b*c], [-2*a*c, -2*a*b]])

print( X + Y )

# iii)
P = Matrix([[-1, 4, -6], [8, 5, 16], [2, 8, 5]])
Q = Matrix([[12, 7, 6], [8, 0, 5], [3, 2, 4]])

print( P + Q )

# iv)
x = sp.symbols('x')

I = Matrix([[cos(x)**2, sin(x)**2], [sin(x)**2, cos(x)**2]])
J = Matrix([[sin(x)**2, cos(x)**2], [cos(x)**2, sin(x)**2]])

print( I + J )

# The solution is going to be:Matrix([[sin(x)**2 + cos(x)**2, sin(x)**2 + cos(x)**2], [sin(x)**2 + cos(x)**2, sin(x)**2 + cos(x)**2]])
# We are gonna simplify the above matrix using the trigonometric identity sin^2(x) + cos^2(x) = 1 as it was only solved as a matrix question
K = I + J
K.simplify()
print("The simplified matrix is:", K)