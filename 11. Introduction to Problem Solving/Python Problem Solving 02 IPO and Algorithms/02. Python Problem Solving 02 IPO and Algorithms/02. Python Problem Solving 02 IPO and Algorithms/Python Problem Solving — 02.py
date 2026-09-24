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
    
#7. Repeated Character Report
string=input("Enter paragraph:")
for char in string:
    count=0
    for i in string:
        if char==i:
            count+=1
    if count>1:        
        if count==2:
            print(char, ":", count, "Duplicate")
        elif 3<=count<=4:
            print(char, ":", count, "Repeated")   
        else:
            print(char, ":", count, "Highly Repeated")     



#8. Shopping Cart Analyzer
total_price=0
budget_count=regular_count=premium_count=luxury_count=0
for i in range(8):
    price=float(input("Enter price:"))
    total_price+=price
    if price<500:
        budget_count+=1
        print("Budget")
    elif price<2000:
        regular_count+=1
        print("Regular")    
    elif price<5000:
        premium_count+=1
        print("Premium")   
    else:
        luxury_count+=1
        print("Luxury")    
avg=total_price/8
print("The total price is:",total_price)    
print("no of items in Budget price is:",budget_count)             
print("no of items in regular price is:",regular_count)             
print("no of items in premium price is:",premium_count)             
print("no of items in luxury price is:",luxury_count)    
print("Average product price is:",avg)         



#9. Character Position Challenge
string=input("Enter paragraph:")
position=0
vowel_count=consonant_count=digit_count=specialchar_count=0
for i in string:
    print("character is:",i,"there position is:",position,end=" ")
    if position%2==0:
        print("position is even",end=" ")
    else:
        print("position is odd",end=" ")
    if i in "AEIOUaeiou":
        vowel_count+=1
        print("and character is vowel")
    elif "A" <= i <= "Z" or "a" <= i <= "z":
        consonant_count+= 1
        print("and character is consonant")
    elif chr(48)<=i<=chr(57):
        digit_count+=1  
        print("and character is digit")
    else:
        specialchar_count+=1  
        print("and character is special")
    position+=1    
print("in string vowel is:",vowel_count)              
print("in string consonant is:",consonant_count)              
print("in string digit is:",digit_count)              
print("in string special character is:",specialchar_count)              



#10. Number Pattern With Conditions
n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(1,i*2+2):
        if (j)%3==0 and (j)%5==0:
            print("Z",end=" ")
        elif (j)%3==0:
            print("X",end=" ") 
        elif (j)%5==0:
            print("Y",end=" ") 
        else:   
            print(j,end=" ")
    print()    



#11. Username Analyzer
for i in range(5):
    is_len=is_first_char=is_digit=is_underscore=is_invalid_schar=False
    digit_count=underscore_count=0
    user_name=input("Enter your user name:")
    if len(user_name)>=8:
        is_len=True
    first_char=user_name[0]   
    if chr(65)<=first_char<=chr(90):
        is_first_char=True
    for i in user_name:
        if chr(48)<=i<=chr(57):    
            digit_count+=1
            is_digit=True
        elif i==chr(95):   
            underscore_count+=1
            is_underscore=True
        else:
            is_invalid_schar=True
    score=int(is_len)+int(is_first_char)+int(is_digit)+int(is_underscore)+int(is_invalid_schar) 
    if score==5:
        print("Valid")    
    elif 3<=score<=4:
        print("Needs Improvement")    
    else:
        print("Invalid")    
    print("the length of username is:",len(user_name))    
    print("number of digit in username is:",digit_count)
    print("number of underscore in username is:",underscore_count)
            


#12. Vowel-Consonant Battle
sentence=input("Enter sentence:")
vowel_count=consonant_count=0
acount=ecount=icount=ocount=ucount=0
for i in sentence:
    if i in "Aa":
        acount+=1
        vowel_count+=1
    elif i in "Ee":
        ecount+=1
        vowel_count+=1
    elif i in "Ii":
        icount+=1
        vowel_count+=1   
    elif i in "Oo":
        ocount+=1
        vowel_count+=1 
    elif i in "Uu":
        ucount+=1
        vowel_count+=1        
    else:
        consonant_count+=1
if vowel_count>consonant_count:
    print("Vowels Win")   
elif vowel_count<consonant_count:
    print("Consonants Win")         
else:
    print("Draw")  
print("in string a and A letters frequency is:",acount)              
print("in string e and E letters frequency is:",ecount)              
print("in string i and I letters frequency is:",icount)              
print("in string o and O letters frequency is:",ocount)              
print("in string u and U letters frequency is:",ucount)      



#13. Electricity Bill Calculator
for i in range(6):
    units_used=int(input("Enter units used:"))
    total_revenue=0
    if units_used<=100:
        total_revenue=units_used*5
    elif units_used<=200:
        total_revenue=100*5+(units_used-100)*7
    elif units_used<=400:
        total_revenue=100*5+100*7+(units_used-200)*10
    else:
        total_revenue=100*5+100*7+200*10+(units_used-400)*15
    print("total revenue is:",total_revenue)    
    if total_revenue<1000:
        print("Low")      
    elif total_revenue<3000:
        print("Medium")   
    else:
        print("High")    



#14. Word Character Balance
sentence=input("Enter sentence:")
words=sentence.split()
for word in words:
    vowel_count=consonant_count=other_count=0
    for i in word:
        if i in "AEIOUaeiou":
            vowel_count+=1
        elif "A" <= i <= "Z" or "a" <= i <= "z":
            consonant_count+=1
        else:
            other_count+=1  
    if vowel_count>consonant_count:
        print(f"In this word {word}: Vowel Heavy")   
    elif vowel_count<consonant_count:
        print(f"In this word {word}: Consonant Heavy")         
    else:
        print(f"In this word {word}: Balanced")



#15. Matrix Value Analyzer
even_count=odd_count=positive_count=negative_count=zero_count=large_num=0
for i in range(3):
    for j in range(3):
        num=int(input(f"Enter number for matrix (rows x coloums) {i+1}x{j+1}:"))
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
        if num>0:
            positive_count+=1
        elif num<0:
            negative_count+=1
        else:
            zero_count+=1
        if large_num<num:
            large_num=num
print("even number in matrix is:",even_count)      
print("odd number in matrix is:",odd_count)      
print("positive number in matrix is:",positive_count)      
print("negative number in matrix is:",negative_count)      
print("zero number in matrix is:",zero_count)     
print("largest number in matrix is:",large_num) 
        
#15.extra concept
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]

matrix=[]
for i in range(3):
    arr = list(map(int,input("Enter the Number: ").split()))
    matrix.append(arr)
print(matrix)



#16. Password Character Distribution
password=input("Enter password:")
ucount=lcount=dcount=sccount=0
for i in password:
    if chr(65)<=i<=chr(90):
        ucount+=1
    elif chr(97)<=i<=chr(122):
        lcount+=1    
    elif chr(48)<=i<=chr(57):
        dcount+=1    
    else:
        sccount+=1 
total_char=ucount+lcount+dcount+sccount
print(f"The upper character percantage in password is: {(ucount/total_char)*100}")
print(f"The lower character percantage in password is: {(lcount/total_char)*100}")
print(f"The digit character percantage in password is: {(dcount/total_char)*100}")
print(f"The special character percantage in password is: {(sccount/total_char)*100}")
if (ucount/total_char)*100>(lcount/total_char)*100 and (ucount/total_char)*100>(dcount/total_char)*100 and (ucount/total_char)*100>(sccount/total_char)*100:
    print("upper characters dominates")
elif (lcount/total_char)*100>(ucount/total_char)*100 and (lcount/total_char)*100>(dcount/total_char)*100 and (lcount/total_char)*100>(sccount/total_char)*100:
    print("lower characters dominates")    
elif (dcount/total_char)*100>(lcount/total_char)*100 and (dcount/total_char)*100>(ucount/total_char)*100 and (dcount/total_char)*100>(sccount/total_char)*100:
    print("digits dominates") 
else:
    print("special charcters dominates")  



#17. Student Name and Marks
high_marks=0
topper=""
for i in range(5):
    vowel_count=consonant_count=0
    grade=""
    student_name=input("Enter your name:")
    for word in student_name:
        if word in "AEIOUaeiou":
            vowel_count+=1
        elif "A" <= word <= "Z" or "a" <= word <= "z":
            consonant_count+=1    
    marks=int(input("Enter your marks:"))    
    if 100>=marks>=90:
        grade="A+"
    elif 89>=marks>=75:
        grade="A"  
    elif 74>=marks>=50:
        grade="B"
    elif 35<=marks<50:
        grade="C"
    elif 0<=marks<=34:
        grade="D"
    else:
        print("please marks give in range 0 to 100")  
    print("student get grade is:",grade)          
    if vowel_count>consonant_count:
        print("In students name vowel is more than consonant")      
    else:
        print("In students name consonant is more than vowel")          
    if high_marks<marks:
        high_marks=marks
        topper=student_name  
print(f"the topper in 5 students is {topper} and get marks is:{high_marks}")    



#18. ATM Transaction Analyzer
balance=float(input("Enter present balance:"))
transaction_count=0
for i in range(7):
    Deposit_transaction=int(input(f"Enter number of Deposit in day{i+1}:"))
    Withdrawal_transaction=int(input(f"Enter number in Withdrawal in day{i+1}:"))
    for j in range(Deposit_transaction):
        deposit_money=float(input(f"Enter deposit {j+1} money:"))
        transaction_count+=1
        balance+=deposit_money
    for k in range(Withdrawal_transaction):
        withdrawal_money=float(input(f"Enter withdrawal {k+1} money:"))
        if withdrawal_money>balance:
            print("not enogh money")
        else:
            balance-=withdrawal_money
            transaction_count+=1
        if balance<1000:
            print("Low Balance")     
print("final balance is:",balance)
print("the total number of transactions is:",transaction_count)       




#22. String Compression Counter
string="aaabbccccdd"
acount=bcount=ccount=dcount=0
for i in string:
    if i=="a":
        acount+=1
    elif i=="b":
        bcount+=1
    elif i=="c":
        ccount+=1
    else:
        dcount+=1
print(f"a{acount}b{bcount}c{ccount}d{dcount}")    




#46. Number Box Pattern
n=int(input("Enter number of rows and colums for n*n box:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1:
            print("*",end="")  
        elif 1<i<n:
            if (i+j)%2==0 and 1<j<n:
                print("E",end="")
            elif (i+j)%2!=0 and 1<j<n:
                print("O",end="") 
            else:
                print("*",end="") 
        else:
            print("*",end="")   
    print()                   