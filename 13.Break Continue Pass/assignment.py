#Section A --- Practice Problems on break
#A1. Output Prediction --- Easy
#Q1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")

# 1
# 2
# 3
# 4
# Finished

#Q2
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)

# s
# k
# y

#Q3
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

# 2
# 4
# 6

#A2. Write a Program --- Medium
#Q4
limit = int(input("Enter limit: "))

for i in range(1, limit + 1):
    if i == 7:
        break
    print(i, end=" ")

#Q5
string = input("Enter string: ")
target = input("Enter target character: ")

for ch in string:
    print(ch, end=" ")
    if ch == target:
        break

#Q6
numbers = list(map(int, input("Enter numbers: ").split()))

for n in numbers:
    if n < 0:
        break
    print(n, end=" ")

#A3. Think Carefully --- Challenging
#Q7
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

#Q8
sentence = input("Enter sentence: ").split()
target = input("Enter target word: ")

for word in sentence:
    if word == target:
        print("Found")
        break
else:
    print("Not found")

#Section B --- Practice Problems on continue
#B1. Output Prediction --- Easy
#Q9
for i in range(1, 7):
    if i == 4:
        continue
    print(i)

# 1
# 2
# 3
# 5
# 6

#Q10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

#dctn

#Q11
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# 1
# 2
# 4
# 5

#B2. Write a Program --- Medium
#Q12
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

#Q13
string = input("Enter string: ")
target = input("Enter character to remove: ")
for ch in string:
    if ch == target:
        continue
    print(ch, end="")

#Q14
marks = list(map(int, input("Enter marks: ").split()))
for mark in marks:
    if mark < 40:
        continue
    print(mark, end=" ")

#B3. Think Carefully --- Challenging
#Q15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

#Q16
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

#Q17
word = input("Enter word: ").lower()
count = 0
for ch in word:
    if ch in "aeiou":
        continue
    count += 1
print(count)

#Section C --- Practice Problems on for-else
#C1. Output Prediction --- Easy
#Q18
for i in range(1, 4):
    print(i)
else:
    print("Done")

# 1
# 2
# 3
# Done

#Q19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

# 1
# 3
# 4
# Completed

#Q20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

# 1
# 2
# Outside loop

#Q21
for item in []:
    print("Inside")
else:
    print("Else block")

# Else block

#C2. Write a Program --- Medium
#Q22
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for n in numbers:
    if n == target:
        print("Found")
        break
else:
    print("Not found")

#Q23
string = input("Enter string: ")
target = input("Enter character: ")

for ch in string:
    if ch == target:
        print("Character exists")
        break
else:
    print("Character missing")

#Q24
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

#C3. Think Carefully --- Challenging
#Q25
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")

#All are even

#Q26
#CASE-A
for x in range(3):
    continue
else:
    print("A")

#A

#CASE-B
for x in range(3):
    break
else:
    print("B")

#No Output

#CASE-C
for x in range(0):
    print(x)
else:
    print("C")

#C

#Q27
string = input("Enter string: ")

for ch in string:
    if string.count(ch) >= 2:
        print(ch)
        break
else:
    print("No repeated character")

#Section D --- Practice Problems on pass
#D1. Output Prediction --- Easy
#Q28
for i in range(1, 4):
    if i == 2:
        pass
    print(i)

# 1
# 2
# 3

#Q29
x = 10
if x > 5:
    pass
print("Finished")

#Finished

#Q30
for letter in "cat":
    pass

print("Loop ended")

#Loop ended

#D2. Write a Program --- Medium
#Q31
for i in range(1, 6):
    if i % 2 == 0:
        pass
    print(i)

#Q32
choice = int(input("Enter choice (1, 2, or 9): "))

if choice == 1:
    print("Option 1 selected")
elif choice == 2:
    pass
else:
    print("Unknown option")
print("Program closed")

#D3. Think Carefully --- Challenging
#Q33
#Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

# 1
# 2
# 3
# 4

#Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# 1
# 2
# 4

#Q34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#Section E --- Mixed Challenge Questions
#Q35
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")

# 1
# 3

#Q36
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for n in numbers:
    if n < 0:
        continue
    if n == target:
        print("Target found")
        break
else:
    print("Target not found")

#Q37
numbers = list(map(int, input("Enter numbers: ").split()))

for n in numbers:
    if n == 0:
        continue
    if n == -1:
        break
    print(n)
else:
    print("All values processed")

#Q38
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed

#Q39
numbers = list(map(int, input("Enter numbers: ").split()))

for n in numbers:
    if n < 0:
        continue
    if n % 4 == 0 and n % 6 == 0:
        print("Found:", n)
        break
else:
    print("No matching number")

#Q40
  # No.	                 Correct answer	Explanation
# 1	break	     Stops searching immediately after finding a username.
# 2	continue	 Skips a blank string and processes the remaining strings.
# 3	for-else	 Displays "Not found" if the loop finishes without break.
# 4	pass	     Acts as a placeholder in an unfinished function.
# 5	continue	 Skips the current number and moves to the next iteration.
# 6	break	     Stops the loop when the sentinel value is encountered.
# 7	for-else	 Reports that all items were checked if the loop finishes without break.
# 8	pass	     Keeps an otherwise empty conditional block syntactically valid.

# Examples to remember
# 1. break
for name in ["Aman", "Ravi", "Neha"]:
    if name == "Ravi":
        print("Found")
        break

# 2. continue
for word in ["hello", "", "python"]:
    if word == "":
        continue
    print(word)

# 3. for-else
for n in [2, 4, 6]:
    if n == 5:
        print("Found")
        break
else:
    print("Not found")

# 4. pass
def future_function():
    pass