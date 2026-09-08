is_student = input("Are you a student? (True/False): ")
has_id = input("Do you have an ID? (True/False): ")
has_ticket = input("Do you have a ticket? (True/False): ")

if is_student == "True" and has_id == "True" and has_ticket == "True":
    print("Allowed")
else:
    print("Not Allowed")