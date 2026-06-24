import sympy as sp 
import numpy as np
from sympy import symbols, Matrix, Rational, sqrt

x = sp.symbols('x')

#Question 3
# If a matrix has 18 elements, what are the possible orders it can have? What if it has 5 elements?

def find_orders(num_elements):
    orders = []
    for i in range(1, num_elements + 1):
        if num_elements % i == 0:
            j = num_elements // i
            orders.append((i, j))
    return orders

print("Possible orders for 18 elements:", find_orders(18))
print("Possible orders for 5 elements:", find_orders(5))

#The solution is as follows:
# Possible orders for 18 elements: [(1, 18), (2, 9  ), (3, 6), (6, 3), (9, 2), (18, 1)]
# Possible orders for 5 elements: [(1, 5), (5, 1)]