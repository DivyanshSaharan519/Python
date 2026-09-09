odd_sum=0
n=int(input("Enter n: "))
for i in range(1,n+1):
    if i%2!=0:
        odd_sum=odd_sum+i
print(f"Odd Sum = {odd_sum}")