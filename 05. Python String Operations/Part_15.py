    # PART 15 - Error Identification

# Task 37A - IndexError

text = "Python"

try:
    print(text[20])
except IndexError:
    print("IndexError: String index is out of range.")


# Task 37B - TypeError

try:
    text[0] = "J"
except TypeError:
    print("TypeError: Strings are immutable.")


# Task 37C - TypeError

age = 20

try:
    print("Age: " + age)
except TypeError:
    print("TypeError: Cannot concatenate string and integer.")


# Task 37D - ValueError

try:
    print(text.index("Java"))
except ValueError:
    print("ValueError: Java was not found in the string.")