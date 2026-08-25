print("\n--- Task 19: Error Handling ---")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero: ZeroDivisionError")

try:
    print("Hello" - "World")
except TypeError:
    print("Invalid string arithmetic: TypeError")

try:
    print(None + 10)
except TypeError:
    print("Arithmetic with None: TypeError")
