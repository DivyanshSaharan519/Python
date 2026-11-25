# Section A — Understand Recursion (10 marks)


# 1. Predict the output (2 marks)

def show(n):
    if n==0:
        print("Stop")
        return
    print(n)
    show(n-1)
    print(n)
show(2)

# Write the exact output, line by line.

# output ==> 2
           # 1
           # Stop
           # 1
           # 2

# 2. Find the base case (2 marks)
# In this function, identify the base case and explain why it stops recursion.

def total(n):
    if n==0:
        return 0
    return n + total(n-1)

# Answer ==> The base case is 
# if n==0:
#     return 0

# 3. Find the bug (3 marks)

# Explain why this function does not reach its base case when called with count(2). Rewrite the incorrect line.

# INCORRECT LINE: count(n + 1)

# def count(n):
#     if n==0:
#         return
#     count(n+1)

# CORRECT LINE: count(n - 1)

def count(n):
    if n==0:
        return
    count(n-1)

# 4. Print or return? (3 marks)
# What does this function return when called as answer(3)? Explain why.

# INCORRECT LINE: n + answer(n - 1)

# def answer(n):
#     if n==0:
#         return 0
#     n + answer(n-1)
# print(answer(3))

# CORRECT LINE: return n + answer(n - 1)

def answer(n):
    if n==0:
        return 0
    return n + answer(n-1)
print(answer(3))


# Section B — Basic Recursive Problems (30 marks)


# 5. Count down (4 marks)
# Write countdown(n) that prints every integer from n down to 1, then prints "Done!".
# Constraint: n is a non-negative integer.

# Examples:
# countdown(3)

# Output:
# 3
# 2
# 1
# Done!

# Edge case: countdown(0) should print only Done!.

def countdown(n):
    if n==0:
        print("Done!")
        return
    print(n)
    countdown(n-1)
countdown(3)

# 6. Count up (4 marks)
# Write count_up(n) that prints numbers from 1 through n in ascending order.

# Examples:
# count_up(4)

# Output:
# 1
# 2
# 3
# 4

# Edge case: count_up(0) should print nothing.

def count_up(n):
    if n==0:
       return
    count_up(n-1)
    print(n)
count_up(4)

# 7. Sum from 1 to n (4 marks)
# Write sum_to(n) that returns the sum of all integers from 1 through n.

# Examples:
# print(sum_to(5))  # 15
# print(sum_to(0))  # 0
# Constraint: n is a non-negative integer.

def sum_to(n):
    if n==0:
        return 0
    return n + sum_to(n-1)
print(sum_to(5))
print(sum_to(0))

# 8. Factorial (4 marks)
# Write factorial(n) that returns n!.

# Examples:
# print(factorial(4))  # 24
# print(factorial(0))  # 1
# Constraint: n is a non-negative integer.

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
print(factorial(4))
print(factorial(0))

# 9. Sum of digits (4 marks)
# Write digit_sum(n) that returns the sum of the digits of a non-negative integer.

# Examples:
# print(digit_sum(583))  # 16
# print(digit_sum(7))    # 7
# print(digit_sum(0))    # 0
# Hint: % 10 gets the last digit; // 10 removes the last digit.

def digit_sum(n):
    if n==0:
        return 0
    return (n%10)+digit_sum(n//10)
print(digit_sum(583))
print(digit_sum(7))
print(digit_sum(0))

# 10. Power (5 marks)
# Write power(base, exponent) that returns base raised to exponent.

# Examples:
# print(power(2, 5))  # 32
# print(power(9, 0))  # 1
# print(power(3, 1))  # 3
# Constraint: exponent is a non-negative integer. Do not use ** in your function.

def power(base, exponent):
    if exponent==0:
        return 1
    return base * power(base, exponent - 1)
print(power(2, 5))
print(power(9, 0))
print(power(3, 1))

# 11. Count digits (5 marks)
# Write count_digits(n) that returns the number of digits in a non-negative integer.

# Examples:
# print(count_digits(5382))  # 4
# print(count_digits(6))     # 1
# print(count_digits(0))     # 1
# Hint: Each recursive call removes the last digit using // 10. Be careful with 0.

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(5382))
print(count_digits(6))
print(count_digits(0))


# Section C — Apply and Analyze (20 marks)


# 12. Reverse a number as a string (5 marks)
# Write reverse_text(text) that returns the characters of a string in reverse order using recursion.

# Examples:
# print(reverse_text("cat"))  # "tac"
# print(reverse_text("a"))    # "a"
# print(reverse_text(""))     # ""
# Hint: Take the last character and combine it with the reverse of the remaining string,
# or take the first character and place it after the reversed remainder.

def reverse_text(text):
    if len(text) == 0:
        return ""
    return text[-1] + reverse_text(text[:-1])
print(reverse_text("cat"))
print(reverse_text("a"))
print(reverse_text(""))

# 13. Fibonacci number (5 marks)
# Write fibonacci(n) that returns the nth Fibonacci number using these definitions:
# fibonacci(0) = 0
# fibonacci(1) = 1
# Otherwise, fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)

# Examples:
# print(fibonacci(0))  # 0
# print(fibonacci(1))  # 1
# print(fibonacci(6))  # 8
# Constraint: n is a non-negative integer. Test only small values because this basic recursive method repeats calculations.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(6))

# 14. Find the maximum digit (5 marks)
# Write max_digit(n) that returns the largest digit in a non-negative integer.

# Examples:
# print(max_digit(4729))  # 9
# print(max_digit(555))   # 5
# print(max_digit(0))     # 0
# Constraint: Do not use max(), loops, or convert the number to a string.
# Hint: Compare the last digit (n % 10) with the maximum digit in the remaining number (n // 10).
# Design the base case carefully.

def max_digit(n):
    if n < 10:
        return n
    max_of_rest = max_digit(n // 10)
    if n % 10 > max_of_rest:
        return n % 10
    return max_of_rest
print(max_digit(4729))
print(max_digit(555))
print(max_digit(0))

# 15. Trace the return values (5 marks)
# Without running the code, write the value returned by mystery(4) and show the return calculation.

def mystery(n):
    if n<=1:
        return n
    return mystery(n-1) + mystery(n-2)

# Also state the values returned by mystery(0), mystery(1), and mystery(2).

# Answer ==>
# mystery(0) returns 0
# mystery(1) returns 1
# mystery(2) returns 1
# mystery(4) returns 3


# Section D — Edge Cases and Debugging (10 marks)


# 16. Fix the factorial (3 marks)
# This function gives the wrong result for factorial(0). Fix the base case.

# Incorrect function:
# def factorial(n):
#     if n==0:
#         return 0
#     return n * factorial(n-1)

# Corrected function:
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

# 17. Make progress (3 marks)
# The function below never changes n. Rewrite it so it counts down to 0 and stops.

# Incorrect function:
# def stop_at_zero(n):
#     if n==0:
#         return
#     stop_at_zero(n)

# Corrected function:
def stop_at_zero(n):
    if n==0:
        return
    stop_at_zero(n-1)

# 18. State the limitation (4 marks)
# Explain what may happen if a recursive function makes too many nested calls. Name the Python error that can occur.
# Give one reason a loop may be a better choice for a very large counting task.

# Answer ==> Answer: If a recursive function makes too many nested calls, it may use too much memory and exceed Python's
# recursion limit. Python can raise a RecursionError.