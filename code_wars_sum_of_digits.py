def digital_root(n):
    # Keep adding the contents of n until the len = 1
    answer = 0

    """
    Take input -> turn int to string -> split to array -> have running count of total -> keep computing until len(total) = 1
    x = 942
    z = str(x)
    y = z.split()
    
    y is an array containing the each digit in the initial param.
    Need to recursively call length check while also creating new array of the new sum
    
    total  = 0
    while 
    for i in y:
        for x in i:
            total = total + int(x)
    
    print(total)
    """
    
