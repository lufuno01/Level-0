def common_characters(first_word, second_word):
    first_word.lower()
    common_letters = []
    second_word.lower()
    for letters in first_word:
        if letters in second_word:
            common_letters.append(letters)
            results = ", ".join(common_letters)

    print(results)


common_characters("House", "Computer")

