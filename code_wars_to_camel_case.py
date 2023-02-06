def to_camel_case(text):
    if text == "" or text == " ":
        return('')
    
    text_array = text.replace('-', ' ')
    text_array = text_array.replace('_', ' ')
    text_array = text_array.split(' ')
    first_letter_first_word = text_array[0][0]
    text_array_2 = []
    index = 1
    
    
    
    if first_letter_first_word != first_letter_first_word.capitalize():
        text_array_2.append(text_array[0])
    else:
        text_array_2.append(text_array[0])
        
    while index != len(text_array):
        text_array_2.append(text_array[index].capitalize())
        index = index + 1
    
    answer_string = "".join(text_array_2)
    return answer_string
