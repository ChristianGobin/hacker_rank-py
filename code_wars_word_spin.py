# Function reverses all words of array and returns a reversed string.
# Get to spin the words that are of len 5 or greater.


def reverse_word(_str):
  answer = [word for word in _str.split(" ")]
  for word in answer:
    if len(word) >= 5:
      
  print(answer)
  
  
def flip_word(some_var):
    index = len(some_var)
    flipped_word_array = []
    while index > 0:
        flipped_word_array.append(some_var[index - 1])
        index = index - 1
    flipped_word = "".join(flipped_word_array)
    return(flipped_word)
