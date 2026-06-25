import sympy as sp 
import numpy as np

from sympy import sin, cos, trigsimp, symbols

# Question 13
# Its a trigonometric matrix which has to be proved
# F(X)*F(Y) = F( X + Y )

x, y = symbols("x , y")

# The equation is:

Fx = sp.Matrix([[cos(x), -sin(x), 0], [sin(x), cos(x), 0], [0, 0, 1]])


Fy = sp.Matrix([[cos(y), -sin(y), 0], [sin(y), cos(y), 0], [0, 0, 1]])


# For the LHS part we have F(x)*F(y), so we are defining LHS first

LHS = Fx * Fy 

print("LHS =", LHS )

LHS = sp.trigsimp(LHS)

print("LHS =", LHS )

# Now that we have LHS we can find out RHS which is F( x + y ) and define the RHS.
# At first I tried to do fx + fy but it didnt work lol then I took the help of AI and explained me what mistake I did in the code

RHS = sp.Matrix([[cos( x + y ), -sin( x + y ), 0], [sin( x + y ), cos(  x + y ), 0], [0, 0, 1]])

print("RHS =", RHS )

RHS = sp.trigsimp(RHS)

print("RHS =", RHS )

# We got our answers for both the sides now we just have to verify it 

if LHS == RHS:
    print("Verified = F(x) * F(y) = F( x + y )")
else:
    print("Not Verified")