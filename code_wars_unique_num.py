def find_uniq(arr):
    for i in arr:
        if arr.count(i) == 1:
            n = i
    return n   # n: unique integer in the array
