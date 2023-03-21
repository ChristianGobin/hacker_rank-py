def solution(number):
    tally = 0
    for item in range(number):
        if item % 3 == 0 or item % 5 == 0:
            tally = tally + item
    return tally
