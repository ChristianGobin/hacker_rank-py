def is_valid_walk(walk):
    def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    count_n = 0
    count_s = 0
    count_w = 0
    count_e = 0
    
    for item in walk:
        if item == 'n': 
            count_n = count_n + 1
        elif item == 's': 
            count_s = count_s + 1
        elif item == 'w': 
            count_w = count_w + 1
        elif item == 'e': 
            count_e = count_e + 1
    
    if count_n == count_s and count_w == count_e:
        return True
    else:
        return False
        
            
            
            
 """
 Solved
 """
