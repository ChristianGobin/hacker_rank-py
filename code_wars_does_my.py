#!/usr/bin/env python3
def narcissistic( value ):
	pow = len(str(value))
	ans_arr = []
	for i in str(value) :
		ans_arr.append(int(i) ** pow)
		print(ans_arr)
	
	sum_ans = sum(ans_arr)
	if sum_ans == value:
		return True
	return False


