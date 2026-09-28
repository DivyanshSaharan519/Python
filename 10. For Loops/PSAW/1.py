# 1. 3x3 Star Grid
n = int(input("1. Enter size: "))
i = 0

while i < n:
    j = 0
    while j < n:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# 2. Numbers in Rows
n = int(input("2. Enter size: "))
i = 0

while i < n:
    j = 1
    while j <= n:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# 3. Row Numbers
n = int(input("3. Enter size: "))
i = 1

while i <= n:
    j = 0
    while j < n:
        print(i, end=" ")
        j += 1
    print()
    i += 1


# 4. Increasing Star Pattern
n = int(input("4. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# 5. Decreasing Star Pattern
n = int(input("5. Enter rows: "))
i = n

while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1


# 6. Increasing Number Pattern
n = int(input("6. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# 7. Repeated Number Pattern
n = int(input("7. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1


# 8. Multiplication Tables
n = int(input("8. Enter number of tables: "))
m = int(input("Enter multiples: "))
i = 1

while i <= n:
    j = 1
    while j <= m:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1


# 9. Multiplication Grid
rows = int(input("9. Enter rows: "))
cols = int(input("Enter columns: "))
i = 1

while i <= rows:
    j = 1
    while j <= cols:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1


# 10. Squares in Rows
rows = int(input("10. Enter rows: "))
n = int(input("Enter numbers: "))
i = 0

while i < rows:
    j = 1
    while j <= n:
        print(j * j, end=" ")
        j += 1
    print()
    i += 1


# 11. Alphabet Pattern
n = int(input("11. Enter rows: "))
i = 1

while i <= n:
    j = 0
    while j < i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i += 1


# 12. Repeated Alphabet Pattern
n = int(input("12. Enter rows: "))
i = 0

while i < n:
    j = 0
    while j <= i:
        print(chr(65 + i), end=" ")
        j += 1
    print()
    i += 1


# 13. Odd Number Pattern
n = int(input("13. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(2 * j - 1, end=" ")
        j += 1
    print()
    i += 1


# 14. Even Number Pattern
n = int(input("14. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(2 * j, end=" ")
        j += 1
    print()
    i += 1


# 15. 5x5 Star Square
n = int(input("15. Enter size: "))
i = 0

while i < n:
    j = 0
    while j < n:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# 16. 5x5 Number Square
n = int(input("16. Enter size: "))
i = 0

while i < n:
    j = 1
    while j <= n:
        print(j, end=" ")
        j += 1
    print()
    i += 1


# 17. Row-wise Numbers
n = int(input("17. Enter size: "))
i = 0
num = 1

while i < n:
    j = 0
    while j < n:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1


# 18. Print 1 to N in Rows
rows = int(input("18. Enter rows: "))
cols = int(input("Enter numbers per row: "))
i = 0
num = 1

while i < rows:
    j = 0
    while j < cols:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1


# 19. Coordinate Pairs
n = int(input("19. Enter size: "))
i = 1

while i <= n:
    j = 1
    while j <= n:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1


# 20. All Number Combinations
n = int(input("20. Enter range: "))
i = 1

while i <= n:
    j = 1
    while j <= n:
        print(i, j)
        j += 1
    i += 1


# 21. Multiplication Grid
n = int(input("21. Enter size: "))
i = 1

while i <= n:
    j = 1
    while j <= n:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1


# 22. Repeated Number Pattern
n = int(input("22. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i += 1


# 23. Decreasing Number Pattern
n = int(input("23. Enter starting number: "))
i = n

while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1


# 24. Reverse Number Pattern
n = int(input("24. Enter starting number: "))
i = n

while i >= 1:
    j = n
    while j >= n - i + 1:
        print(j, end="")
        j -= 1
    print()
    i -= 1


# 25. Repeated Row Number Pattern
n = int(input("25. Enter rows: "))
i = 1

while i <= n:
    j = 1
    while j <= n:
        print(i, end="")
        j += 1
    print()
    i += 1