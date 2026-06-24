import sympy as sp 
import numpy as np
from sympy import symbols, Matrix, Rational, sqrt

x = sp.symbols('x')

#Question 2
# If a matrix has 24 elements, what are the possible orders it can have ? what if it has 13 elements ?

def find_orders(num_elements):
    orders = []
    for i in range(1, num_elements + 1):
        if num_elements % i == 0:
            j = num_elements // i
            orders.append((i, j))
    return orders

print("Possible orders for 24 elements:", find_orders(24))
print("Possible orders for 13 elements:", find_orders(13))

# Possible orders for 24 elements: [(1, 24), (2, 12), (3, 8), (4, 6), (6, 4), (8, 3), (12, 2), (24, 1)]
# Possible orders for 13 elements: [(1, 13), (13, 1)]