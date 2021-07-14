#!/usr/bin/env python3
def fizzbuzz(n):
	final_array = []
	for i in range(1, n+1):
		if(i % 3 == 0 and i % 5 == 0 and i != 0):
			final_array.append("FizzBuzz")
		elif(i % 3 == 0 and i % 5 != 0):
			final_array.append("Fizz")
		elif(i % 5 == 0 and i % 3 != 0):
			final_array.append("Buzz")
		else:
			final_array.append(i)
	return final_array


print(fizzbuzz(5))