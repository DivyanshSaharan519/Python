char=input("Enter a character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")