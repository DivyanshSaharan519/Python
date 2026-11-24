# Beginner


# 1. Create a function with a local variable city and print it.

# def city():
#     city = "Jodhpur"
#     print(city)
# city()

# 2. Create a global variable school. Read it inside a function.

# school = "Vidhyashram International School"
# def school_name():
#     print(school)
# school_name()

# 3. Assign a variable inside an if block and print it outside the block.

# if True:
#     name = "praveen"
# print(name)

# 4. Use a for loop to assign a loop variable. Print it after the loop.

# for i in range(5):
#     print(i)
# print("After loop:", i)

# 5. Explain the difference between scope and lifetime in your own words.

# Scope refers to the region of the code where a variable is accessible,
# while lifetime refers to the duration for which a variable exists in memory.


# Intermediate


# 6. Predict the output:

# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)

# output==>200
#          100

# 7. Fix this code so it increments the global variable:

# INCORRECT CODE:
# clicks = 0
# def click():
#     clicks += 1

# CORRECT CODE:
# clicks = 0
# def click():
#     global clicks
#     clicks += 1
# click()
# print(clicks)

# 8. Explain why this code raises an error:

# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# Answer: The error occurs because 'name' is used before assigning a value inside the function.
# Python treats it as a local variable, causing an UnboundLocalError.
# To fix it, use the global keyword or remove the assignment.

# 9. Write a nested function that reads a variable from its enclosing function.

# def outer():
#     x = 10
#     def inner():
#         print(x)
#     inner()
# outer()

# 10. Write a function that returns a list. Show that the returned list can be changed by the caller.

# def get_list():
#     return [1, 2, 3]
# list = get_list()
# list.append(4)
# print(list)
 
# Output==>[1, 2, 3, 4]


# Challenging


# 11. Use nonlocal to create a counter that returns 1, 2, 3 across three calls.

# def make_counter():
#     count=0
#     def increment():
#         nonlocal count
#         count+=1
#         return count
#     return increment
# counter=make_counter()
# print(counter())
# print(counter())
# print(counter())

# Output==>1
#          2
#          3

# 12. Predict the output: python

# x=1
# def outer():
#     x=2
#     def inner():
#         x=3
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

# Output==>3
#          2
#          1

# 13. Explain why the loop variable in a normal for loop can remain available after the loop,
# but a list-comprehension variable in Python 3 does not overwrite an outer variable.

# Answer: In a normal for loop, the loop variable remains available after
# the loop because it does not have a separate scope. But in Python 3,
# a list-comprehension variable has its own scope, so it does not change the
# outer variable.

# 14. Create a function that returns another function. Explain which variable remains available and why.

# def outer():
#     name = "Asha"
#     def inner():
#         print(name)
#     return inner
# my_function = outer()
# my_function()

# The variable name remains available because the inner function remembers the variable from the outer function.
# This is called a closure.

# 15. Explain why variable names such as list, str, and sum should usually be avoided.

# Answer: Variable names like list, str, and sum should usually be avoided
# because they are already built-in names in Python. Using them as variable names
# can overwrite their original functions and cause confusion or errors. It is better to
# use names like my_list, text, and total.