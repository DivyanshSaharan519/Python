# PART 16 - Practical Challenge
# Task 38 - Name Processor

name = input("Enter your full name: ")

cleaned_name = name.strip()

print("Original input:", name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First character:", cleaned_name[0])
print("Last character:", cleaned_name[-1])

character = input("Enter a character to search: ")

print("Character exists:", character in cleaned_name)