# PART 10 - Searching

# Task 20 - Membership

text = "Python is a programming language"

print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)


# Task 21 - find()

print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))


# Task 22 - index()

print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))

# Java is not present, so index() gives ValueError.
# print(text.index("Java"))


# Task 23 - Count Characters

text = "banana"

print(text.count("a"))
print(text.count("n"))
print(text.count("b"))


# Task 24 - Starts and Ends

filename = "student_notes.pdf"

print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))