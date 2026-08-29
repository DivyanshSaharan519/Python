# PART 11 - Replacing

# Task 25 - Replace a Word

text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)


# Task 26 - Multiple Replacements

text = "apple apple apple"

print(text.replace("apple", "mango"))


# Task 27 - Limited Replacement

text = "apple apple apple"

print(text.replace("apple", "mango", 1))


# Task 28 - Check Immutability

text = "Python"

text.upper()

print(text)

text = text.upper()

print(text)