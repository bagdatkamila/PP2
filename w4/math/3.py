"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625

Apothem = [(length of one side)/{2 ×(tan(180/number of sides))}].
Step 5: Now, find the area of the regular polygon using the formula, Area = (number of sides × length of one side × apothem)/2.
"""
from math import *

n = int(input("Input number of sides: "))
l = float(input("Input the lenght of a side: "))
apothem = l/(2*tan(pi/n))
area = int((n * l * apothem)/2)

print("The area of the polygon is: ", area)