a = int(input("Enter a number: "))

if a < 0:
    print("Negative")
elif a <= 10:
    print("Number is between 0 and 10")
elif a <= 50:
    print("Number is between 11 and 50")
elif a <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")