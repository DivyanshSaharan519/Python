even_sum=0
n=int(input("Enter n: "))
for i in range(1,n+1):
    if i%2==0:
        even_sum=even_sum+i
print(f"Even Sum = {even_sum}")