"""
def validate_pin(pin):
    my_pin = [int(c) for c in pin]
    if(len(my_pin) != 4 and len(my_pin) != 6):
        return false
        bool_pin_check = [item.isdigit() for item in my_pin]
        print(bool_pin_check)
    else:
        for item in my_pin:
            if(item.isdigit() == True):
                return true
            else:
                return false
   
print(validate_pin("1234"))
"""
my_input = "1351"
my_input_transformed = [int(c) for c in my_input]
for i in my_input_transformed:
    if(type(i) == int):
        print(True)
is_a_number = type(my_input_transformed)
print(is_a_number)
print(my_input_transformed)
print(len(my_input_transformed))
length_of_input = len(my_input_transformed)

if length_of_input != 4 and length_of_input != 6:
    print(False)
else:

    print(True)
    
 #Check if all items in list are digits. 
