num=int(input("Enter a number: "))
if num%2==0 and num>0:
    print("Positive even number")
elif num%2==0 and num<0:
    print("Negative even number")
elif num%2!=0 and num>0:    
    print("Positive odd number")
elif num%2!=0 and num<0:
    print("Negative odd number")
else:
    print("Zero")