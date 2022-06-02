
def checking_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    no_duplicates_found = []
    vowels_found = []
    word.lower()
    for x in word:
        if x in vowels:
            vowels_found.append(x)

    for i in vowels_found:
        if i not in no_duplicates_found:
            no_duplicates_found.append(i)
    results = ", ".join(no_duplicates_found)
    print(results)


checking_vowels("Umuzi")
   
  
