#!/usr/bin/env python3
# Data Types
f = 2.0 #float
i = 1 #int
s = "String"
b = True

# Functions and Math

mass = 50 #kg
initial_velocity = 30 #m/s
acceleration = -9.8 #m/s^2
time = 6 #seconds

"""
Function uses a kinematic equation to find final velocity of a moving body, given: v0, acceleration, time(s)
"""
def find_final_velocity(mass, initial_velocity, acceleration, time):
	final_velocity = initial_velocity + (acceleration * time)
	print("The Final Velocity = " + str(final_velocity) + " m/s")
	return final_velocity

find_final_velocity(mass, initial_velocity, acceleration, time)

"""
Array Methods
sort
reverse
pop
insert

"""
integer_array = [22, 43, 11, 54, 90]
integer_array.sort(reverse = True)
integer_array.append("S")
integer_array.clear()

