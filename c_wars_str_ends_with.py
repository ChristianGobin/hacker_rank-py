def solution(string, ending):
    end_len = len(ending) - 1
    str_len = len(string) - 1
    
    # slice notation.
    # get 
    if ending in string and string[end_len : -1] == ending:
        return True 
    return False

# Thinking: Take slice of string from end and check if equal to ending string
# Also handle the empty string error. Should be True not false// All the time
