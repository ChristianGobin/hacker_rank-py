if __name__ == '__main__':
    s = input()
    
    is_alphannumeric = True #isalnum
    is_alphabetical = True #isalpha
    is_adigit = True #isdigit
    is_lower = True #islower
    is_upper = True #isupper
    
    for l in s:
        if l.isalnum() == True:
            print(is_alphannumeric)
        elif l.isalpha() == True:
            print(is_alphabetical)
        elif l.isdigit() == True:
            print(is_adigit)
        elif l.islower() == True:
            print(is_lower)
        elif l.isupper() == True:
            print(is_upper)
        else:
            print(False)