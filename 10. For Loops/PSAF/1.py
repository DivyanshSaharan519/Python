# 1. 3x3 Star Grid
n = int(input("1. Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# 2. Numbers in Rows
n = int(input("2. Enter size: "))

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()


# 3. Row Numbers
n = int(input("3. Enter size: "))

for i in range(1, n + 1):
    for j in range(n):
        print(i, end=" ")
    print()


# 4. Increasing Star Pattern
n = int(input("4. Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 5. Decreasing Star Pattern
n = int(input("5. Enter rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 6. Increasing Number Pattern
n = int(input("6. Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 7. Repeated Number Pattern
n = int(input("7. Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


# 8. Multiplication Tables
n = int(input("8. Enter number of tables: "))
m = int(input("Enter multiples: "))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i * j, end=" ")
    print()


# 9. Multiplication Grid
rows = int(input("9. Enter rows: "))
cols = int(input("Enter columns: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(i * j, end=" ")
    print()


# 10. Squares in Rows
rows = int(input("10. Enter rows: "))
n = int(input("Enter numbers: "))

for i in range(rows):
    for j in range(1, n + 1):
        print(j * j, end=" ")
    print()


# 11. Alphabet Pattern
n = int(input("11. Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# 12. Repeated Alphabet Pattern
n = int(input("12. Enter rows: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


# 13. Odd Number Pattern
n = int(input("13. Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()


# 14. Even Number Pattern
n = int(input("14. Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()


# 15. 5x5 Star Square
n = int(input("15. Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# 16. 5x5 Number Square
n = int(input("16. Enter size: "))

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()


# 17. Row-wise Numbers
n = int(input("17. Enter size: "))
num = 1

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num += 1
    print()


# 18. Print 1 to N in Rows
rows = int(input("18. Enter rows: "))
cols = int(input("Enter numbers per row: "))

num = 1

for i in range(rows):
    for j in range(cols):
        print(num, end=" ")
        num += 1
    print()


# 19. Coordinate Pairs
n = int(input("19. Enter size: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i},{j})", end=" ")
    print()


# 20. All Number Combinations
n = int(input("20. Enter range: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, j)


# 21. 10x10 Multiplication Grid
n = int(input("21. Enter size: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()


# 22. Repeated Number Pattern
n = int(input("22. Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()


# 23. Decreasing Number Pattern
n = int(input("23. Enter starting number: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 24. Reverse Number Pattern
n = int(input("24. Enter starting number: "))

for i in range(n, 0, -1):
    for j in range(n, n - i, -1):
        print(j, end="")
    print()


# 25. Repeated Row Number Pattern
n = int(input("25. Enter rows: "))

for i in range(1, n + 1):
    for j in range(n):
        print(i, end="")
    print()