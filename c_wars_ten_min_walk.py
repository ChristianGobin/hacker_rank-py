def is_valid_walk(walk):
    for item in walk:
        
            
            
            
 """
 
 1 - Check Length of Walk: Must be 10.
 2 - Check Count of Directions given, ex. count of n == count of south: assert that we returned to the beginning of the route due to equal travel
 3 - Anything else is false.
 
 def is_valid_walk(walk):
    count_n = 0
    count_s = 0
    count_w = 0
    count_e = 0
    
    if len(walk) > 10 or len(walk) < 10:
        return False
    else:
        
        for item in walk:
            if walk[item] == 'n':
                count_n = count_n + 1
            if walk[item] == 's':
                count_s = count_s + 1
            if walk[item] == 'w':
                count_w = count_w + 1
            if walk[item] == 'e':
                count_e = count_e + 1
    
        if count_n == count_s and count_w == count_e:
            return True
        else:
            return False
  
 
 """
