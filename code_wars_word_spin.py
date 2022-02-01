# Function reverses all words of array and returns a reversed string.
# Get to spin the words that are of len 5 or greater.


def reverse_word(_str):
  answer = [word for word in _str.split(" ")]
  for word in answer:
    if len(word) >= 5:
      
  print(answer)
  
  
def reverses_string(_str):
  reversed = []
  index = len(_str)
  while index > 0:
    reversed.append(_str[index - 1])
    index = index - 1
  
  reversed_string = ""
  reversed_string = reversed_string.join(reversed)
  print(reversed_string)

reverse_word("Kid Gobin")