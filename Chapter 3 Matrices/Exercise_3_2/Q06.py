import sympy as sp 
import numpy as np 
from sympy import cos, sin, tan, cot, csc, sec, symbols
# Question number 6

# We are computing a trigonometric matrix

θ = sp.symbols("θ")

A = cos(θ) * sp.Matrix([[cos(θ), sin(θ)], [-sin(θ), cos(θ)]]) + sin(θ) * sp.Matrix([[sin(θ), -cos(θ)], [cos(θ), sin(θ)]])

print(A)


# we can simplify it further

print(sp.simplify(A))