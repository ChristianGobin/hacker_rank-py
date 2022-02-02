# Function reverses all words of array and returns a reversed string.
# Get to spin the words that are of len 5 or greater.


def spin_words(sentence):
    sentence = sentence.split(" ")
    answer = " "
    for index, word in enumerate(sentence):
        if len(word) >= 5:
            sentence[index] = flip_word(word)
    answer = answer.join(sentence)
    return answer


def flip_word(some_var):
    index = len(some_var)
    flipped_word_array = []
    while index > 0:
        flipped_word_array.append(some_var[index - 1])
        index = index - 1
    flipped_word = "".join(flipped_word_array)
    return(flipped_word)
