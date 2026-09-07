marks = int(input("Enter marks: "))

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 60:
    print("Average")
elif marks >= 40:
    print("Below Average")
elif marks >= 33:
    print("Pass")
else:
    print("Fail")