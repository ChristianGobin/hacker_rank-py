my_str = "Hello"
def reverse(_str):
  reversed = []
  index = len(_str)
  while index > 0:
    reversed.append(_str[index - 1])
    index = index - 1
  
  reversed_string = ""
  reversed_string = reversed_string.join(reversed)
  print reversed_string


reverse("Hello world as")
