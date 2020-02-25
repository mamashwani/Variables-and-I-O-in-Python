# -*- coding: utf-8 -*-
"""
Muhammad Mashwani 1378052
Assignment #1
COSC 1306 
"""
import math

PI = math.pi

radius = float(input("Enter radius for a circle: "))

circle_area = PI*radius**2
hex_area = 3*((3**(1/2)/2)*(radius**2))
shaded_area = circle_area - hex_area
#need blank space here
print("You entered: ",radius)

print("="*40)
print("Circle  area  = ",circle_area)
print("Hexagon area  = ",hex_area)
print("Shaded  area  = ",shaded_area)
print("="*40)
 #for first bonus need to find a number betwen one eand ten (1.83)
 # the radius value 1.839871 returns a value for the shaded area that is six degits precise to the radius.
 

print(1378052 + radius)

#the radius value for which my PSID plus the radius value equals the shaded area is 1593.225966