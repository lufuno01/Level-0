
def checking_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    no_duplicates_found = []
    vowels_found = []
    word.lower()
    for item in word:
        if item in vowels:
            vowels_found.append(item)

    for word in vowels_found:
        if word not in no_duplicates_found:
            no_duplicates_found.append(word)
    results = ", ".join(no_duplicates_found)
    print(results)


checking_vowels("Umuzi")
