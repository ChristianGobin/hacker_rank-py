#!/usr/bin/env python3
# Example: input 9119 -> 811181
def square_digits(num_str):
	digit_arr = num_str.split()
	
	return "".join([i**2 for i in digit_arr])
		
	
	
	
	
	
	
print(square_digits("9112"))