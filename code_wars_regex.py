"""
Constraints:
    Pin's must be 4 or 6 digits long.
    Data Type of characters must ONLY be digits.
"""

def validate_pin(pin):
    pin_length = len(pin) #get pin length
    true_array = [] #store boolean value after checking data type of pin characters
    if pin_length != 4 and pin_length != 6: #check pin length
        return False
    else:
        for char in pin: #test data type of character in pin
        #append bool value to array that represents if each character is a digit
            if char.isdigit() == True:
                true_array.append(True) 
            else:
                true_array.append(False)
    
    #check if array of booleans contains any false values,
    #any false value in array would mean a character in the pin is not a digit and thus not valid
    if False in true_array:
        return False
    else:
        return True

            