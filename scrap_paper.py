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

# List Comprehension with conditionals
basic_numbers = [1,2,3,4,56,73,123,66,32]
doubled_evens = [num * 2 for num in basic_numbers if num % 2 == 0] # Double even number -> append to list

double_evens_odds_plus_one = [num * 2 if num % 2 == 0 else num + 1 for num in basic_numbers] # Double even numbers and add one to odd -> append to list
print(double_evens_odds_plus_one)



#################
def amper_names(names):
	pass
	# names = [{},{},{}] <- an array of hashes
	# need to return different values based on length of hash array.


	
	
# *args takes any number of params and stores in tuple called args
def print_items(*args):
	for i in args:
		print(i)




class Person:
	def __init__(self) -> None:
		self.name = "Unnamed"
		self.age = 0
	
	def say_name():
		print(self.name)

John = Person()
John.say_name()
