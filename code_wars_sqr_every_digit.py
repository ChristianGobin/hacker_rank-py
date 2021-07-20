#!/usr/bin/env python3
# Example: input int 9119 -> int 811181
def square_digits(str_num_seq): 
    str_num_seq_1 = [x for x in str(str_num_seq)] # make int into int array [x, i ,j ,k]
    arr_of_nums = [str(int(i)**2) for i in str_num_seq_1] # make array of squared int values from first array, store as string array. ['x.' , 'i.', 'j.', 'k.']
    answer = int("".join(arr_of_nums)) # join string together to make one number -> convert joined string to int
    return answer

