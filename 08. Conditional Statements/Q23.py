age = int(input("Enter age: "))
has_id = input("Do you have ID? (True/False): ") == "True"

if age >= 18 and has_id:
    print("Allowed")