def solution(string, ending):
    if ending in string:
        if ending == '': #special case, empty string returns true.
            return True
        elif ending[-1] == string[-1]: #if last char of ending param is the same as last char of string param, then return true.
            return True
    return False
