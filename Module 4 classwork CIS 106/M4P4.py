# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:06:47 2026

@author: shama
"""

first_name = input("Enter your first name: ")
steps = int(input("Enter the number of steps walked: "))

calories_burned = steps * 0.25

print(f"{first_name} burned {calories_burned:.2f} calories.")