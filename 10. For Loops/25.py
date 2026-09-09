text = input("Enter a string: ")
count = 0
for ch in text:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count += 1
print("Uppercase letters:", count)