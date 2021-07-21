def find_uniq(arr):
    arr.sort() 
    if arr.count(arr[0]) == 1:
        return arr[0]
    else:
        return arr[-1]
    
    """
    
    Explanation:
        Since we know that the array contains atleast 2 unique numbers, we can sort the array and only take the index of the first and last element in the array.
        This would mean that each of the unique elements would naturally be at either end. Finally I take those element indexes and check the array for a count of the elements.
        The element with the count of exactly one is the correct element.
        
    Hacky Answer:
    for i in arr:
        if arr.count(i) is 1:
            n = i
    return n   # n: unique integer in the array
    
    Works but takes too long, needs refactor.
    
    """
