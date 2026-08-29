# PART 12 - Whitespace

# Task 29

text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# Task 30 - User Input

name = input("Enter your name: ")

cleaned_name = name.strip()

print("Cleaned name:", cleaned_name)