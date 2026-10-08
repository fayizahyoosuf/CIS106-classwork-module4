# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:08:46 2026

@author: shama
"""

fixed_costs = float(input("Enter the fixed costs: "))
price_per_unit = float(input("Enter the price per unit: "))
cost_per_unit = float(input("Enter the cost per unit: "))

break_even_point = fixed_costs / (price_per_unit - cost_per_unit)

print(f"Break-even point: {break_even_point:.2f} units")