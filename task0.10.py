def common_characters(first_word, second_word):
    first_word.lower()
    common_letters = []
    second_word.lower()
    for letter in first_word:
        if letter in second_word:
            common_letters.append(letter)
            results = ", ".join(common_letters)

    print(results)


common_characters("House", "Computer")

