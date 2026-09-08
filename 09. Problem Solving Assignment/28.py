name1 = input("Enter first person's name: ")
age1 = int(input("Enter first person's age: "))

name2 = input("Enter second person's name: ")
age2 = int(input("Enter second person's age: "))

name3 = input("Enter third person's name: ")
age3 = int(input("Enter third person's age: "))

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")
elif age1 == age2 and age2 == age3:
    print("All three have the same age")
else:
    print("Two people have the same youngest age")