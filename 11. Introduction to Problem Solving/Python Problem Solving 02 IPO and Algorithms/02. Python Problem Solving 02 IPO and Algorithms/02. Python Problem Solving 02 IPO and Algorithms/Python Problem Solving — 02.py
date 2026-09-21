# Problem 1
# INPUT
#     First number
#     Second number
# PROCESSING
#     Add first number and second number
# OUTPUT
#     addition

# 1. Start
# 2. Read first number
# 3. Read second number
# 4. Add the two numbers
# 5. Store the result
# 6. Display the result
# 7. Stop

# input: = 65
# input: = 55
# result: = add
# output: = 120
# input: = 54
# input: = 46
# result: = add
# output: = 100

a = int(input())
b = int(input())
addition= a + b
print(addition)



# Problem 2
# INPUT:
#   Number
# PROCESSING:
#   check number%2==0 and  number%2==1
# output:
#   even or odd

# start
# read in number
# number%2 in Even
# number%2! in odd
# display result
# stop

# input: = 20
# if input%2==0
# result: = even 
# output: = even 
# input: =21
# elif input%2==1
# result: = odd 
# output: = odd

number=int(input("Enter Your numbbers:"))
if number%2==0:
    print("even")
else:
    print("odd")



# Problem 3
# INPUT:
#   first number 
#   second number
#   three number
# PROCEESING:
#   F>S AND F>T and...
#   compare numbers
# OUTPUT:
#       largest number

# Start.
# Input F, S, T.
# Compare all three.
# Print the largest.
# Stop.

# F= 12
# S = 25
# T = 18
# Largest = 25

from typing import Final


num1= int(input("Enter Your first number: "))
num2 = int(input("Enter Your second number: "))
num3 = int(input("Enter Your third number: "))
if num1 > num2 and num1 > num3:
     print("Largest =", num1)
elif num2 > num1 and num2 > num3:
     print("Largest =", num2)
else:
     print("Largest =", num3)



# Problem 4
# input
#   Age
# Process	
#   Check if age ≥ 18
# Output
#   Eligible or Not Eligible

# Start.
# Input age.
# If age is at least 18, print Eligible.
# Otherwise print Not Eligible.
# Stop.

Age = 20
#Output: Eligible for vote
Age = 15
#Output: Not eligible for vote
age = int(input("Enter Your age: "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")



# Problem 5
# Input
#   Price
# Process
#   Apply 20% discount if price ≥ 2000
# Output
#   Final Price

# Start.
# Input price.
# If price is at least 2000:
# Discount = 20%.
# Final price = price − discount.
# Otherwise final price = price.
# Print final price.
# Stop.

Price = 2500
Discount = 500
FinalPrice = 2000

price = float(input("Enter Your price: "))
if price >= 2000:
  price = price - (price * 20 / 100)
  print("Final Price =", price)
else:
  price=price
  print("Final Price=",price)
	

# Problem 6
# Input
#   Three subject marks
# Process
#   Calculate average
# Output
#   Pass or Fail

# Start.
# Input three marks.
# Calculate average.
# If average is at least 40, print Pass.
# Otherwise print Fail.
# Stop.

# Marks
# 60
# 50
# 40
# Average = (60+50+40)/3 = 50
# Output: Pass

mark1 = int(input("Enter marks of Subject m1: "))
mark2 = int(input("Enter marks of Subject m2: "))
mark3 = int(input("Enter marks of Subject m3: "))
avg = (mark1 + mark2 + mark3) / 3
print("Average =", avg)
if avg >= 40:
    print("Pass")
else:
    print("Fail")