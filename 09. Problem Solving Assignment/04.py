a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print("Smallest number:", a)
elif b < a and b < c:
    print("Smallest number:", b)
else:
    print("Smallest number:", c)