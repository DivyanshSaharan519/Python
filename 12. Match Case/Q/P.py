#Set 1 — Basic match-case
#Q1
choice = 1

match choice:
    case 1:
        print("Add")
    case 2:
        print("Subtract")
    case 3:
        print("Multiply")
    case _:
        print("Invalid")

#Q2
choice = 3

match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")

#Q3
choice = 5

match choice:
    case 1:
        print("A")
    case 2:
        print("B")
    case 3:
        print("C")
    case _:
        print("Invalid")

#Q4
number = 2

match number:
    case 1:
        print("First")
    case 2:
        print("Second")
    case 3:
        print("Third")
    case _:
        print("Unknown")

#Q5
day = 7

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")

#Set 2 — case _

#Q6
value = 10

match value:
    case 5:
        print("Five")
    case 10:
        print("Ten")
    case 15:
        print("Fifteen")
    case _:
        print("Other")

#Q7
value = 20

match value:
    case 5:
        print("Five")
    case 10:
        print("Ten")
    case 15:
        print("Fifteen")
    case _:
        print("Other")

#Q8
choice = 0

match choice:
    case 1:
        print("Start")
    case 2:
        print("Pause")
    case 3:
        print("Stop")
    case _:
        print("Invalid Choice")

#Set 3 — String Matching

#Q9
color = "red"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid")

#Q10
color = "green"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid")

#Q11
command = "start"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "pause":
        print("Pausing")
    case _:
        print("Unknown Command")

#Q12
command = "restart"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case "pause":
        print("Pausing")
    case _:
        print("Unknown Command")

#Set 4 — Multiple Values Using |

#Q13
day = 2

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid")

#Q14
day = 7

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid")

#Q15
number = 4

match number:
    case 1 | 3 | 5:
        print("Odd Group")
    case 2 | 4 | 6:
        print("Even Group")
    case _:
        print("Other")

#Q16
number = 9

match number:
    case 1 | 3 | 5:
        print("Odd Group")
    case 2 | 4 | 6:
        print("Even Group")
    case _:
        print("Other")

#Set 5 — Match-Case with Input

#Q17
choice = int(input("Enter choice: "))
match choice:
    case 1:
        print("Add")
    case 2:
        print("Delete")
    case 3:
        print("Update")
    case _:
        print("Invalid")

#Q18
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Login")
    case 2:
        print("Register")
    case 3:
        print("Profile")
    case _:
        print("Invalid Option")

#Q19
day = int(input("Enter day: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend or Invalid")

#Set 6 — Multiple Print Statements

#Q20
choice = 2

match choice:
    case 1:
        print("First")
        print("Option")
    case 2:
        print("Second")
        print("Option")
    case _:
        print("Invalid")

#Q21
number = 3

match number:
    case 1:
        print("A")
        print("B")
    case 2:
        print("C")
        print("D")
    case 3:
        print("E")
        print("F")
    case _:
        print("X")

#Set 7 — Nested match-case

#Q22
category = "student"
choice = 1

match category:
    case "student":
        match choice:
            case 1:
                print("Courses")
            case 2:
                print("Marks")
            case _:
                print("Invalid Student Choice")

    case "teacher":
        print("Teacher Section")

    case _:
        print("Invalid Category")

#Q23
category = "student"
choice = 2

match category:
    case "student":
        match choice:
            case 1:
                print("Courses")
            case 2:
                print("Marks")
            case _:
                print("Invalid Student Choice")

    case "teacher":
        print("Teacher Section")

    case _:
        print("Invalid Category")

#Q24
category = "teacher"
choice = 1

match category:
    case "student":
        match choice:
            case 1:
                print("Courses")
            case 2:
                print("Marks")

    case "teacher":
        match choice:
            case 1:
                print("Students")
            case 2:
                print("Attendance")

    case _:
        print("Invalid Category")

#Q25
category = "student"
choice = 5

match category:
    case "student":
        match choice:
            case 1:
                print("Courses")
            case 2:
                print("Marks")
            case _:
                print("Invalid Student Choice")

    case "teacher":
        print("Teacher Section")

    case _:
        print("Invalid Category")

#Set 8 — if + match-case

#Q26
choice = 1
age = 20

match choice:
    case 1:
        if age >= 18:
            print("Allowed")
        else:
            print("Not Allowed")

    case 2:
        print("Exit")

    case _:
        print("Invalid")

#Q27
choice = 1
age = 16

match choice:
    case 1:
        if age >= 18:
            print("Allowed")
        else:
            print("Not Allowed")

    case 2:
        print("Exit")

    case _:
        print("Invalid")

#Q28
choice = 2
age = 20

match choice:
    case 1:
        if age >= 18:
            print("Allowed")
        else:
            print("Not Allowed")

    case 2:
        print("Exit")

    case _:
        print("Invalid")
#Set 9 — Match-Case with Simple Expressions

#Q29
a = 10
b = 5
choice = 1

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case _:
        print("Invalid")

#Q30
a = 10
b = 5
choice = 2

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case _:
        print("Invalid")

#Q31
a = 10
b = 5
choice = 3

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case _:
        print("Invalid")

#Set 10 — Slightly Tricky

#Q32
value = 1

match value:
    case 1:
        print("One")
    case 1:
        print("Another One")
    case _:
        print("Other")

#Q33
value = "1"

match value:
    case 1:
        print("Number")
    case "1":
        print("String")
    case _:
        print("Other")

#Q34
value = 0

match value:
    case 1 | 2:
        print("A")
    case 0 | 3:
        print("B")
    case 4:
        print("C")
    case _:
        print("D")

#Q35
value = "green"

match value:
    case "red" | "yellow":
        print("Stop or Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid")

#Challenge Set

#Q36
choice = 2
value = 10

match choice:
    case 1:
        print(value + 5)
    case 2:
        print(value * 2)
    case 3:
        print(value - 3)
    case _:
        print(value)

#Q37
category = "student"
choice = 3

match category:
    case "student":
        match choice:
            case 1:
                print("Course")
            case 2:
                print("Marks")
            case 3:
                print("Attendance")
            case _:
                print("Invalid")

    case "teacher":
        print("Teacher")

    case _:
        print("Unknown")

#Q38
choice = 3
age = 17

match choice:
    case 1:
        if age >= 18:
            print("Adult")
        else:
            print("Minor")

    case 2:
        print("Option 2")

    case 3:
        if age >= 18:
            print("Allowed")
        else:
            print("Not Allowed")

    case _:
        print("Invalid")

#Q39
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Working Day")
    case 6 | 7:
        print("Holiday")
    case _:
        print("Invalid Day")

#Q40
command = "pause"
choice = 2

match command:
    case "start":
        print("Starting")

    case "pause":
        match choice:
            case 1:
                print("Pause Music")
            case 2:
                print("Pause Video")
            case _:
                print("Invalid Pause Choice")

    case "stop":
        print("Stopping")

    case _:
        print("Unknown Command")

#Bonus — Guard Practice
#Q41
marks = 85

match marks:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case _:
        print("Fail")

#Q42
marks = 55

match marks:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case x if x >= 40:
        print("D")
    case _:
        print("Fail")

#Q43
number = -5

match number:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")

#Q44
number = 0

match number:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")