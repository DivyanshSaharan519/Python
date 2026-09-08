a = int(input("Enter a number: "))

if a % 5 == 0 and a % 11 == 0:
    print("Divisible by both 5 and 11")
elif a % 5 == 0:
    print("Divisible only by 5")
elif a % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")