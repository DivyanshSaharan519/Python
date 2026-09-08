char=input("Enter a character: ")
if char.isalpha():
    if char in 'aeiouAEIOU':
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")
else:
    print(char, "Invalid input")