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

# Function uses the kinomatic equation to find final velocity of a moving body, given 4 parameters
def find_final_velocity(mass, initial_velocity, acceleration, time):
	final_velocity = initial_velocity + (acceleration * time)
	print("The Final Velocity = " + str(final_velocity) + " m/s")
	return final_velocity

find_final_velocity(mass, initial_velocity, acceleration, time)