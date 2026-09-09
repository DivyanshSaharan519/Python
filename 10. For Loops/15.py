even_count = 0
n=int(input("Enter a number: "))
for i in range(1, n+1):
    if i % 2 == 0:
        even_count = even_count + 1
print(f"Even Count = {even_count}")