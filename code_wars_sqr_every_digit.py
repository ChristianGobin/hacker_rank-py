#!/usr/bin/env python3
# Example: input 9119 -> 811181
def sqr_nums(str_num_seq):
    arr_of_nums = [str(int(i)**2) for i in str_num_seq]
    answer = "".join(arr_of_nums)
    return answer


some_input = "2234"
sqr_nums(some_input)
