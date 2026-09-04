age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = bool(int(input("Has ID? Enter 1 for True, 0 for False: ")))

if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")