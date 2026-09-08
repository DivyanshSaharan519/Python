m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks")
elif m1 < 35 or m2 < 35 or m3 < 35:
    print("Fail")
else:
    average = (m1 + m2 + m3) / 3

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")