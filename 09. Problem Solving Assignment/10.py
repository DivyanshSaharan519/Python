age=int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age < 18:
    print("Minor")
else:
    print("Adult")