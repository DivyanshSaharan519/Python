amount = float(input("Enter purchase amount: "))

if amount < 500:
    discount = 0
elif amount < 1000:
    discount = 5
elif amount < 2000:
    discount = 10
elif amount < 5000:
    discount = 15
else:
    discount = 20

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Original amount:", amount)
print("Discount percentage:", discount, "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)