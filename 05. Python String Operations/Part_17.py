# PART 17 - Practical Challenge
# Task 39 - Sentence Analyzer

sentence = input("Enter a sentence: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))

words = sentence.split()

print("Number of words:", len(words))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Python exists:", "Python" in sentence)

character = input("Enter a character to count: ")

print("Character count:", sentence.count(character))