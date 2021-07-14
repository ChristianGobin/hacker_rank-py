def validate_pin(pin):
    if(pin.length() != 4 or pin.length() != 6):
        return false
    bool_pin_check = [item.isdigit() for item in pin]
    print(bool_pin_check)
    else:
        for item in pin:
            if(item.isdigit() == True):
                return true
            else:
                return false
   
