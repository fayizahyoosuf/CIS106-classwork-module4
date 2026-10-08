# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:39:58 2026

@author: shama
"""

meal_total = float(input("Enter the total for the meal: "))

tip_15 = meal_total * 0.15
tip_18 = meal_total * 0.18
tip_20 = meal_total * 0.20

print("With 15% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip_15:.2f}")
print(f"Total with Tip {meal_total + tip_15:.2f}")

print()

print("With 18% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip_18:.2f}")
print(f"Total with Tip {meal_total + tip_18:.2f}")

print()

print("With 20% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip_20:.2f}")
print(f"Total with Tip {meal_total + tip_20:.2f}")