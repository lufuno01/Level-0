def common_characters(first_word, second_word):

    for letter in first_word.lower() and second_word.lower():
        if letter in first_word and second_word:
            print(letter, end=",")


common_characters("House", "Computers")
