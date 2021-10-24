def digital_root(n):
    # Find Length of n
    # if n.len > 1 -> continue adding each int of n until n.len = 1
    # input type = non negative int.
    
    # convert n to string then parse then change each item of n back to int
    # finally loop through and add and update n until n.len = 1
    new_n = [int(x) for x in str(n)]
    len_of_n = len(new_n)
    if(len_of_n > 1):
        answer = 0
        while len(new_n) != 1:
            for i in new_n:
                answer += i
                new_n.remove(i)
        return answer
    else:
        return answer



print(digital_root(22))