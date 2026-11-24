# Quick Dry-Run Questions
# 1
def greet():
    print("Hello")
print("Start")
# Output==>Start

# 2
def greet():
    print("Hello")
greet()
greet()
# Output==>Hello Hello

# 3
def first():
    print("A")
def second():
    print("B")
second()
first()
second()
# Output==>B A B

# 4
def show():
    print("Inside")
print("One")
show()
print("Two")
show()
# Output==>One Inside Two Inside

# 5
def outer():
    print("Start")
    print("Middle")
print("A")
outer()
print("B")
# Output==>A Start Middle B

# 6
def task():
    print("Task")
task
print("Done")
# Output==>Done

# 7
def greet():
    print("Hello")
greet()
# Greet() python is case sensitive

# 8
def show():
    print("A")
    print("B")
print("C")
show()
# Output==>C A B



# Coding Practice Problems
# Basic Level
# 1
def greet():
    print("Hello, Python!")
greet()

# 2
def show_name():
    print("Praveen Prajapati")
show_name()
show_name()
show_name()

# 3
def print_line():
    print("-"*20)
print_line()
print("Welcome in Python!")
print_line()

# 4
def show_rules():
    print("do not use mobile phone")
    print("make class room clean")
    print("Pay attention")
show_rules()

# 5
def show_square():
    print("****")
    print("****")
    print("****")
    print("****")
show_square()

# 6
def show_menu():
    print("1.pizza\n2.burger\n3.sandwich")
show_menu()
show_menu()

# 7
def morning_message():
    print("Good Morning!")
def evening_message():
    print("Good Evening!")
evening_message()
morning_message()

# 8
def show_student_card():
    print("Student Card\nPraveen Prajapati\n112513")
show_student_card()

# 9
def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
print_numbers()
print_numbers()

# 10
def show_pattern():
    print("*")
    print("**")
    print("***")
show_pattern()
show_pattern()


# Intermediate Level
# 11
def show_header():
    print("Good Morning")
def show_body():
    print("How are you")
def show_footer():
    print("Nice to meet you")
show_header()
show_body()
show_footer()

# 12
def show_separator():
    print("====================")
show_header()
show_separator()
show_body()
show_separator()
show_footer()

# 13
def step_one():
    print("step one")
def step_two():
    print("step two")
def step_three():
    print("step three")
step_three()
step_one()
step_two()

# 14
def show_table_heading():
    print("Student Name")
show_table_heading()
print("praveen")
print("sheetal")

# 15
def show_star():
    print("*"*5)
show_star()
show_star()
show_star()
show_star()

# 16
def show_welcome():
    print("welcome to python!")
show_welcome()

# 17
def show_help():
    print("""How to Use a Basic Calculator
1. Turn on the device: Press the ON/C or AC (All Clear) button to wake up the screen and reset any old values.
2. Enter the first number: Press the digit keys (0–9) and a decimal point (.) if you need a fraction or decimal.
3. Choose an operation: Press + (addition), - (subtraction), x (multiplication), or / (division).
4. Enter the second number: Type the next set of digits.
5. Get the result: Press the = (equals) button to show the answer""")
show_help()

# 18
def opening_line():
    print("="*30)
    print(" "*5,"MY STORE RECEIPT")
    print("="*30)
def closing_line():
    print("="*30)
    print(" "*5,"THANK YOU!")
    print("="*30)
opening_line()
print("Item: Pen")
print("Price: Rs. 10")
print("Quantity: 2")
print("Total: Rs. 20")
closing_line()

# 19
def print_box():
    print(f"+{"-"*30}+")
    print(f"|{" "*30}|")
    print(f"|{" "*30}|")
    print(f"|{" "*30}|")
    print(f"+{"-"*30}+")
print_box()
print_box()

# 20
def title():
    print("="*30)
    print("       STUDENT PROGRAM")
    print("="*30)
def menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")
def closing_message():
    print("Thank you for using the program!")
    print("Goodbye!")
title()
menu()
closing_message()


# Debugging and Reasoning
# 21
def greet():
    print("Hello")

# 22
def welcome():
    print("Welcome")
welcome()

# 23
# Reason: The function show() is called before it is defined. 
# Python executes code from top to bottom, so it raises a NameError because show has not been defined yet.
def show():
    print("Hello")
show()

# 24
def print_report():
    print("Report")
print_report()
# Print_Report() python is case sensitive

# 25
def a():
    print("A")
def b():
    print("B")
a()
b()
a()
# Output==>A B A

# 26
def message():
    print("Python")
message()
message()
message()
message()
# Output==>4 times

# 27
def example():
    print("One")
    print("Two")
print("Three")
# Output==>line 1 or 2

# 28
# f
# do_task
# student_details
# display_menu

# 29
def name():
    print("praveen")
def class_room():
    print("lab-03")
name()

# 30
def msg():
    print("hello")
print("welcome")
msg()
print("how are you")