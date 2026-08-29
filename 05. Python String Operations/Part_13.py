# PART 13 - Split and Join

# Task 31 - Split

text = "Python is easy to learn"

words = text.split()

print(words)


# Task 32 - Split with Separator

fruits = "apple,banana,mango,orange"

fruit_list = fruits.split(",")

print(fruit_list)


# Task 33 - Join

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# Task 34 - Join with Different Separators

words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))