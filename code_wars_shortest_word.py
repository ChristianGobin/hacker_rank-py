#!/usr/bin/env python3

def find_short(s):
	s_array = s.split(' ')
	lowest_count = len(s_array[0])
	for item in s_array:
		if(len(item) < lowest_count):
			lowest_count = len(item)
	return lowest_count


print(find_short("Hello world it is me!"))