# PART 18 - Final Challenge
# Task 40 - Student Information

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = int(input("Enter age: "))

full_name = first_name + " " + last_name

print("Full Name:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))
print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")
print("Contains Python:", "Python" in course)

new_course = course.replace("Python", "Java")

print("Replaced Course:", new_course)
print("Number of words:", len(course.split()))