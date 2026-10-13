#Topic 1 — Basic Real-Life Choice Problems
#Q1
from typing import Type


choice = 3

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("Sandwich")
    case _:
        print("Invalid choice")


#Q2
choice = 2

match choice:
    case 1:
        print("Wi-Fi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Setting")


#Q3
choice = 2

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change PIN")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")


#Q4
signal = input("Enter signal: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")


#Topic 2 — Practical Menu Systems
#Q4
signal = input("Enter signal: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")


#Q5
choice = 3

match choice:
    case 1:
        print("View Profile")
    case 2:
        print("Vieew Courses")
    case 3:
        print("View Marks")
    case 4:
        print("View Attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid choice")


#Q6
choice = 2

match choice:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")


#Q7
choice = 4

match choice:
    case 1:
        print("Account Balance")
    case 2:
        print("Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case 5:
        print("Customer Support")
    case _:
        print("Invalid choice")


#Q8
choice = 3

match choice:
    case 1:
        print("Morning Show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening Show")
    case 4:
        print("Night Show")
    case _:
        print("Invalid choice")


#Topic 3 — String-Based Real-Life Problems
#Q9
Weather = input("Enter weather: ").lower()

match Weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Invalid Signal")


#Q10
payment = input("Enter payment method: ").lower()

match payment:
    case "upi":
        print("UPI Payment Selected")
    case "card":
        print("Card Payment Selected")
    case "cash":
        print("Cash Payment Selected")
    case "wallet":
        print("Wallet Payment Selected")
    case _:
        print("Invalid Payment Method")


#Q11
FileType = input("Enter File type: ").lower()

match FileType:
    case "pdf":
        print("Document")
    case "jpg":
        print("Image")
    case "png":
        print("Image")
    case "mp3":
        print("Audio")
    case "mp4":
        print("Video")
    case _:
        print("Invalid file type")


#Q12
role = input("Enter role: ").lower()

match role:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Teacher Dashboard")
    case "student":
        print("Student Dashboard")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid Role")


#Topic 4 — Multiple Values Using |
#Q13
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")


#Q14
priority = int(input("Enter priority: "))

match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
    case _:
        print("Invalid Priority")


#Q15
level = int(input("Enter membership level: "))

match level:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Invalid Membership")


#Topic 5 — Nested match-case
#Q16
user = int(input("Enter user type: "))

match user:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Student Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Entering Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Teacher Option")

    case _:
        print("Invalid User Type")


#Q17
account = int(input("Enter account type: "))

match account:
    case 1:
        print("Savings Account")
        operation = int(input("Enter operation: "))
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")

    case 2:
        print("Current Account")
        operation = int(input("Enter operation: "))
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")

    case _:
        print("Invalid Account Type")


#Q18
category = int(input("Enter category: "))

match category:
    case 1:
        product = int(input("Enter product: "))
        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Product")

    case 2:
        product = int(input("Enter product: "))
        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Product")

    case _:
        print("Invalid Category")


#Q19.
category = int(input("Enter category: "))

match category:
    case 1:
        food = int(input("Enter food: "))
        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Food")

    case 2:
        food = int(input("Enter food: "))
        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Food")

    case _:
        print("Invalid Category")


#Topic 6 — match-case with Simple Calculations
#Q20
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print("Result =", a + b)
    case "-":
        print("Result =", a - b)
    case "*":
        print("Result =", a * b)
    case "/":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid Operator")


#Q21
choice = int(input("Enter choice: "))
temperature = float(input("Enter temperature: "))

match choice:
    case 1:
        result = (temperature * 9 / 5) + 32
        print("Temperature =", result, "F")
    case 2:
        result = (temperature - 32) * 5 / 9
        print("Temperature =", result, "C")
    case _:
        print("Invalid Choice")


#Q22
choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        print(value * 1000, "meters")
    case 2:
        print(value / 1000, "kilometers")
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid Choice")


#Topic 7 — match-case + if
#Q23
account = int(input("Enter account type: "))

match account:
    case 1:
        print("Savings Account")
        amount = float(input("Enter amount: "))
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case 2:
        print("Current Account")
        amount = float(input("Enter amount: "))
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case _:
        print("Invalid Account Type")


#Q24
choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
        else:
            print("You are not eligible to start the exam")
    case 2:
        print("Viewing Result")
    case 3:
        print("Exiting Exam Portal")
    case _:
        print("Invalid Choice")


#Q25
ticket = int(input("Enter ticket type: "))
age = int(input("Enter age: "))

match ticket:
    case 1:
        if age < 5:
            print("Free Entry")
        else:
            print("Regular Ticket Selected")
    case 2:
        if age < 5:
            print("Free Entry")
        else:
            print("Premium Ticket Selected")
    case 3:
        if age < 5:
            print("Free Entry")
        else:
            print("VIP Ticket Selected")
    case _:
        print("Invalid Ticket Type")


#Topic 8 — Real-World Application Problems
#Q26
device = int(input("Enter device: "))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")


#Q27
department = int(input("Enter department: "))

match department:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")


#Q28
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exiting Railway System")
    case _:
        print("Invalid Choice")


#Q29
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Searching Book")
    case 2:
        print("Issuing Book")
    case 3:
        print("Returning Book")
    case 4:
        print("Viewing Issued Books")
    case 5:
        print("Exiting Library System")
    case _:
        print("Invalid Choice")


#Q30
status = input("Enter status: ").lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Unknown Order Status")


#Topic 9 — More Challenging Problems
#Q31
banking = int(input("Enter banking type: "))

match banking:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")


#Q32
role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Marks")
            case 2:
                print("Opening Student Attendance")
            case 3:
                print("Opening Student Homework")
            case _:
                print("Invalid Student Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Entering Marks")
            case 2:
                print("Opening Teacher Attendance")
            case 3:
                print("Assigning Homework")
            case _:
                print("Invalid Teacher Option")

    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Child Marks")
            case 2:
                print("Opening Child Attendance")
            case 3:
                print("Contacting Teacher")
            case _:
                print("Invalid Parent Option")

    case _:
        print("Invalid Role")


#Q33
transport = int(input("Enter transport: "))

match transport:
    case 1:
        option = int(input("Enter class: "))
        match option:
            case 1:
                print("Flight Economy Selected")
            case 2:
                print("Flight Business Selected")
            case _:
                print("Invalid Flight Class")

    case 2:
        option = int(input("Enter class: "))
        match option:
            case 1:
                print("Train Sleeper Selected")
            case 2:
                print("Train AC Selected")
            case _:
                print("Invalid Train Class")

    case 3:
        option = int(input("Enter class: "))
        match option:
            case 1:
                print("Bus Ordinary Selected")
            case 2:
                print("Bus Volvo Selected")
            case _:
                print("Invalid Bus Class")

    case _:
        print("Invalid Transport")


#Q34
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        setting = int(input("1. Sound\n2. Graphics\n3. Controls\nEnter setting: "))
        match setting:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")
    case 4:
        print("Exiting Game")
    case _:
        print("Invalid Choice")


#Topic 10 — Challenge Problems
#Q35
category = int(input("Enter category: "))

match category:
    case 1:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Starter")

    case 2:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Main Course")

    case 3:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Dessert")

    case 4:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Drink")

    case _:
        print("Invalid Category")


#Q36
payment = int(input("Enter payment type: "))

match payment:
    case 1:
        option = int(input("1. Scan QR\n2. Enter UPI ID\nEnter option: "))
        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid UPI Option")

    case 2:
        option = int(input("1. Credit Card\n2. Debit Card\nEnter option: "))
        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Card Option")

    case 3:
        option = int(input("1. Add Money\n2. Pay Using Wallet\nEnter option: "))
        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Wallet Option")

    case _:
        print("Invalid Payment Type")


#37
category = int(input("Enter category: "))

match category:
    case 1:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Programming Course")

    case 2:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Mathematics Course")

    case 3:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Communication Course")

    case _:
        print("Invalid Category")


#Q38
choice = int(input("Enter option: "))

match choice:
    case 1:
        option = int(input("1. Start\n2. Stop\nEnter option: "))
        match option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Engine Option")

    case 2:
        option = int(input("1. Headlights\n2. Indicators\n3. Hazard Lights\nEnter option: "))
        match option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Light Option")

    case 3:
        option = int(input("1. Play\n2. Pause\n3. Next\n4. Previous\nEnter option: "))
        match option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Song")
            case 4:
                print("Previous Song")
            case _:
                print("Invalid Music Option")

    case 4:
        option = int(input("1. Start Navigation\n2. Stop Navigation\nEnter option: "))
        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Navigation Option")

    case _:
        print("Invalid Choice")


#Topic 11 — Mixed Logic Challenge
#Q39
role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Employee Profile")
            case 2:
                days = int(input("Enter leave days: "))
                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Opening Employee Salary")
            case _:
                print("Invalid Employee Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Opening Reports")
            case _:
                print("Invalid Manager Option")

    case _:
        print("Invalid Role")


role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Student Option")

    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Teacher Option")

    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Fees")
            case 2:
                print("Opening Admissions")
            case 3:
                print("Opening Notices")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Administration Option")

    case _:
        print("Invalid Role")