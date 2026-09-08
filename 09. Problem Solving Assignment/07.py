a = int(input("Enter a number: "))

if a % 3 == 0 and a % 7 == 0:
    print("Divisible by both 3 and 7")
elif a % 3 == 0:
    print("Divisible only by 3")
elif a % 7 == 0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")