# Dry-Run Questions
# 1
def greet(name):
    print("Hello", name)
greet("Asha")
greet("Rahul")
# Output==>Hello Asha 
# Output==>Hello Rahul

# 2
def subtract(a, b):
    return a - b
print(subtract(8, 3))
print(subtract(3, 8))
# Output==>5 -5

# 3
def calculate(number):
    return number * 2
result = calculate(5)
print(result + 3)
# Output==>13

# 4
def greet(name="Guest"):
    return "Hello " + name
print(greet())
print(greet("Asha"))
# Output==>Hello Guest
# Output==>Hello Asha

# 5
def values():
    return 10, 20
a, b = values()
print(a + b)
# Output==>30

# 6
def show(a, b=5):
    print(a, b)
show(10)
show(10, 20)
show(a=7, b=3)
# Output==>10 5
# Output==>10 20
# Output==>7 3

# 7
def demo():
    print("A")
    return 5
    print("B")
print(demo())
# Output==>A 5

# 8
def total(a, b, c=10):
    return a + b + c
print(total(1, c=3, b=2))
# Output==>6



# Practice Problems
# Beginner
# 1
def welcome():
    print("Welcome to Python")
welcome()
welcome()
welcome()

# 2
def greet(name):
    print("hello"+" "+name)
greet("praveen")

# 3
def show_number(number):
    print(number)
show_number(5)

# 4
def add(a, b):
    return a+b
print(add(1,2))

# 5
def square(number):
    return number*number
print(square(5))

# 6
def is_even(number):
    return number%2==0
print(is_even(4))

# 7
def get_full_name(first_name, last_name):
    return first_name+" "+last_name
print(get_full_name("praveen","prajapati"))

# 8
def introduce(name, city="Pune"):
    return f"{name} is belong to {city}"
print(introduce("surya"))
print(introduce("rohit","mumbai"))

# 9
def subtract(a, b):
    return a-b
print(subtract(1,9))
print(subtract(9,1))

# 10
def get_min_max(a, b):
    if a>b:
        max=a
        min=b
        return max,min
    else:
        max=b
        min=a
        return max,min
max,min=get_min_max(5,1)
print("max :",max)
print("min :",min)


# Intermediate
# 11
def calculate(a, b):
    sum=a+b
    difference=a-b
    product=a*b
    quotient=a/b
    return sum,difference,product,quotient
sum,difference,product,quotient=calculate(5,3)
print(sum,difference,product,quotient)

# 12
def count_digits(number):
    digit_count=0
    if number==0:
        digit_count+=1
    while number>0:
        digit_count+=1
        number=number//10
    return digit_count
print(count_digits(0))

# 13
def classify_number(number):
    if number>0:
        return "Positive"
    elif number<0:
        return "Negative"
    else:
        return "Zero"
print(classify_number(0))
print(classify_number(10))
print(classify_number(-10))

# 14
def calculate_total(price, quantity=1):
    total_price=price*quantity
    return total_price
print(calculate_total(56))
print(calculate_total(9999,5))

# 15
def create_email(username, domain="example.com"):
    return f"{username}@{domain}"
print(create_email("praveen"))
print(create_email("praveen", "gmail.com"))

# 16
def format_name(first, last, uppercase=False):
    if uppercase:
        first=first.upper()
        last=last.upper()
    return f"{first} {last}"
print(format_name("praveen","prajapati"))
print(format_name("praveen","prajapati",True))

# 17
def percentage(marks, total=100):
    return (marks/total)*100
print(percentage(95))
print(percentage(417,500))

# 18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes*seconds_per_minute
print(convert_minutes(5))

# 19
def student_details(name, age, city):
    return name,age,city
print(student_details(age=17,city="Nagaur",name="Praveen"))

# 20
def bill(item, quantity=1, price=100):
    return f"{quantity} {item}'s has total bill is {quantity*price}"
print(bill("pen",5,10))
print(bill(item="pencil",quantity=5,price=10))


# Challenging
# 21
def analyze_number(number):
    if number>=0:
        absolute_value=number
    else:
        absolute_value=-number
    is_even=number%2==0
    digit_count=0
    if number==0:
        digit_count+=1
    while number>0:
        digit_count+=1
        number=number//10
    else:
        if number<0:
            number=-number    
            while number>0:
                digit_count+=1
                number=number//10
    return absolute_value, is_even, digit_count
print(analyze_number(-246))

# 22
def calculate_stats(a, b, c):
    smallest = a
    largest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    total = a + b + c
    return smallest, largest, total
print(calculate_stats(10, 5, 20))

# 23
def make_sentence(subject, verb, object):
    return f"{subject} {verb} {object}."
sentence = make_sentence(object="a book", subject="praveen", verb="reads")
print(sentence)

# 24
def apply_discount(price, discount=0):
    final_price=price-price*discount/100
    return final_price
print(apply_discount(100,10))

# 25
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus
print(calculate_pay(5,20,50))
print(calculate_pay(rate=500,bonus=20,hours=5))

# 26
def get_coordinates(x=0, y=0):
    return x,y
print(get_coordinates())
print(get_coordinates(x=5))
print(get_coordinates(y=10))

# 27
def compare(a, b):
    if a > b:
        result = "A is greater"
    elif b > a:
        result = "B is greater"
    else:
        result = "Equal"
    difference = a - b if a >= b else b - a
    return result, difference
print(compare(10, 5))
print(compare(3, 8))
print(compare(6, 6))

# 28
def convert_temperature(value, scale="C"):
    if scale == "C":
        return (value * 9/5) + 32
    else:
        return (value - 32) * 5/9
print(convert_temperature(25))
print(convert_temperature(77, scale="F"))

# 29
def calculate_result(marks, passing_marks=35):
    if marks>=passing_marks:
        return "Pass"
    else:
        return "Fail"
print(calculate_result(35))

# 30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    total = (quantity * price) + delivery_fee
    return f"{quantity} item has total bill :{total}"
print(order_summary("Book"))
print(order_summary("Book", delivery_fee=20))