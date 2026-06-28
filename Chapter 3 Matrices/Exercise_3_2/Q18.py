import sympy as sp
import numpy as np
from sympy import sin, cos, tan

# Question 18
# We have to prove the two equations are equal or not:
# I + A = (I - A)[[cos(alpha), -sin(alpha)], [sin(alpha),  cos(alpha)]]

alpha = sp.symbols('alpha')

# LHS side equations:

A = sp.Matrix([[0, -tan(alpha/2)], [tan(alpha/2), 0]])

I = sp.eye(2)

# RHS side equations:
B = sp.Matrix([[cos(alpha), -sin(alpha)], [sin(alpha),  cos(alpha)]])

# LHS

LHS = I + A

print("LHS =")

print(LHS)

# RHS

RHS = (I - A) * B

print("RHS =")

print(RHS)

# Simplify the difference directly


X = sp.trigsimp(LHS - RHS)


# Sympy is still confused so we are rewriting tan(alpha/2) {I solved the question 2 times and still I wasnt able to solve it so finally I took AI's help sorry}


X = X.applyfunc(lambda expr: expr.rewrite(sp.sin).simplify())

print("LHS - RHS =")

print(X)

# Lets finish it and verify it 
if X == sp.zeros(2):
    print("Hence, proved")
else:
    print("Not proved")

# I have finished this excercise 3.2 I am not continuing the remaining 4 questions as those are very high level probably (Outside my league) and also they are word problems...Maybe later when I have the experinece I will try to solve the remaining 4
