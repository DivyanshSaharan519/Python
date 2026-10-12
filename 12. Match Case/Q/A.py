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
