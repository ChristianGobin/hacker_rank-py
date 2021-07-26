def solution(string, ending):
    last_letter = string[-1]
    last_ending= ending[-1]
    if ending in string:
        if last_letter == last_ending:
            return True
    return False
