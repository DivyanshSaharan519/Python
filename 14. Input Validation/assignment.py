#Part A — Intermediate Problems
#P1
marks = int(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks! Enter between 0 and 100.")
    marks = int(input("Enter marks: "))
print("Accepted marks:", marks)

#P2
num = int(input("Enter a positive integer: "))
while num <= 0:
    print("Invalid number! Number must be greater than 0.")
    num = int(input("Enter a positive integer: "))
print("Accepted number:", num)

#P3
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Invalid age! Enter age between 0 and 120.")
    age = int(input("Enter your age: "))
print("Accepted age:", age)

#P4
choice = 0
while choice < 1 or choice > 4:
    print("\n1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice < 1 or choice > 4:
        print("Invalid choice! Try again.")
print("Selected option:", choice)

#P5
password = input("Enter password: ").strip()
while len(password) < 8:
    print("Password must contain at least 8 characters.")
    password = input("Enter password: ").strip()
print("Password accepted!")

#P6
temp = float(input("Enter temperature (-20 to 45): "))
while temp < -20 or temp > 45:
    print("Invalid temperature!")
    temp = float(input("Enter temperature (-20 to 45): "))
print("Accepted temperature:", temp)

#P7
balance = 5000
amount = float(input("Enter withdrawal amount: "))
while amount <= 0 or amount > balance:
    print("Invalid amount! Enter an amount greater than 0 and up to", balance)
    amount = float(input("Enter withdrawal amount: "))
balance = balance - amount
print("Withdrawal successful!")
print("Remaining balance: ₹", balance)

#P8
username = input("Enter username: ").strip()
while len(username) < 5 or " " in username:
    print("Invalid username!")
    print("Username needs at least 5 characters and no internal spaces.")
    username = input("Enter username: ").strip()
print("Accepted username:", username)

#P9
num = int(input("Enter a positive number divisible by 3 and 5: "))
while num <= 0 or num % 3 != 0 or num % 5 != 0:
    print("Invalid number!")
    num = int(input("Enter a positive number divisible by 3 and 5: "))
print("Accepted number:", num)

#P10
secret_pin = 2468
attempts = 0
correct = False
while attempts < 3 and not correct:
    pin = int(input("Enter PIN: "))
    attempts = attempts + 1
    if pin == secret_pin:
        correct = True
        print("Access granted!")
    else:
        print("Incorrect PIN!")
if not correct:
    print("Access denied!")

#P11
num = int(input("Enter an integer (10-50): "))
while num < 10 or num > 50:
    print("Invalid number!")
    num = int(input("Enter an integer (10-50): "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#P12
balance = 2000
amount = float(input("Enter deposit amount: "))
while amount <= 0:
    print("Invalid amount! Deposit must be greater than 0.")
    amount = float(input("Enter deposit amount: "))
balance = balance + amount
print("Deposit successful!")
print("New balance: ₹", balance)

#Part B — Challenging Problems
#P13
num = int(input("Enter an integer (1-100): "))
while num < 1 or num > 100:
    print("Invalid number! Enter between 1 and 100.")
    num = int(input("Enter an integer (1-100): "))
print("Accepted number:", num)

#P14
marks = int(input("Enter marks (0-100): "))
while marks < 0 or marks > 100:
    print("Invalid marks!")
    marks = int(input("Enter marks (0-100): "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

#P15
username = input("Enter username: ").strip()
password = input("Enter password: ")
while (len(username) < 5 or " " in username
       or len(password) < 8 or password.strip() == ""):
    print("Invalid username or password!")
    print("Username: minimum 5 characters, no internal spaces.")
    print("Password: minimum 8 characters, not blank.")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")
print("Username and password accepted!")

#P15
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator!")
    operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
while operator == "/" and num2 == 0:
    print("Cannot divide by zero!")
    num2 = float(input("Enter second number again: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2
print("Result:", result)

#P17
balance = 10000
choice = 0
while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current balance: ₹", balance)
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        while amount <= 0:
            print("Deposit must be greater than 0.")
            amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        while amount <= 0 or amount > balance:
            print("Invalid withdrawal amount!")
            amount = float(input("Enter withdrawal amount: "))
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance: ₹", balance)
    elif choice == 4:
        print("Thank you for using the banking system!")
    else:
        print("Invalid menu choice!")

#P18
month = int(input("Enter month number (1-12): "))
day = int(input("Enter day number (1-31): "))
while month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid month or day!")
    month = int(input("Enter month number (1-12): "))
    day = int(input("Enter day number (1-31): "))
print("Accepted month:", month)
print("Accepted day:", day)

#P19
quantity = int(input("Enter product quantity: "))
while quantity <= 0:
    print("Quantity must be a positive integer.")
    quantity = int(input("Enter product quantity: "))
price = float(input("Enter unit price: "))
while price <= 0:
    print("Price must be greater than 0.")
    price = float(input("Enter unit price: "))
total = quantity * price
print("Total cost: ₹", total)

#P20
count = int(input("How many numbers (1-20)? "))
while count < 1 or count > 20:
    print("Invalid count! Enter between 1 and 20.")
    count = int(input("How many numbers (1-20)? "))
total = 0
i = 1
while i <= count:
    num = float(input("Enter number " + str(i) + ": "))
    total = total + num
    i = i + 1
average = total / count
print("Average:", average)

#P21
password = input("Enter password: ")
while True:
    upper = False
    lower = False
    digit = False
    whitespace = False
    for ch in password:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
        if ch.isdigit():
            digit = True
        if ch.isspace():
            whitespace = True
    valid = True
    if len(password) < 8:
        print("Password must have at least 8 characters.")
        valid = False
    if not upper:
        print("Password must contain an uppercase letter.")
        valid = False
    if not lower:
        print("Password must contain a lowercase letter.")
        valid = False
    if not digit:
        print("Password must contain a digit.")
        valid = False
    if whitespace:
        print("Password must not contain whitespace.")
        valid = False
    if valid:
        break
    password = input("Enter password again: ")
print("Strong password accepted!")

#P22
num = int(input("Enter an integer (1-10): "))
while num < 1 or num > 10:
    print("Invalid number!")
    num = int(input("Enter an integer (1-10): "))
print("Accepted number:", num)

#P23
score1 = int(input("Enter score 1 (0-100): "))
while score1 < 0 or score1 > 100:
    print("Invalid score!")
    score1 = int(input("Enter score 1 (0-100): "))
score2 = int(input("Enter score 2 (0-100): "))
while score2 < 0 or score2 > 100:
    print("Invalid score!")
    score2 = int(input("Enter score 2 (0-100): "))
score3 = int(input("Enter score 3 (0-100): "))
while score3 < 0 or score3 > 100:
    print("Invalid score!")
    score3 = int(input("Enter score 3 (0-100): "))
total = score1 + score2 + score3
average = total / 3
print("Total:", total)
print("Average:", average)

#P24
balance = 10000
amount = int(input("Enter withdrawal amount: "))
while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid amount!")
    print("Amount must be positive, within balance, and a multiple of ₹100.")
    amount = int(input("Enter withdrawal amount: "))
balance = balance - amount
print("Withdrawn amount: ₹", amount)
print("Remaining balance: ₹", balance)