#!/usr/bin/env python3
def is_valid_walk(walk):
	n_count = 0
	s_count = 0
	e_count = 0
	w_count = 0
	#determine if walk is valid
	if len(walk) > 10 or len(walk) < 10:
		return False
	for item in walk:
		if item == 'n':
			n_count = n_count + 1
		if item == 's':
			s_count = s_count + 1
		if item == 'e':
			e_count = e_count + 1
		if item == 'w':
			w_count = w_count + 1
			
	if(n_count == s_count) and (e_count == w_count):
		return True
	return False