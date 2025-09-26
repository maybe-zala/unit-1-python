students : dict = {}
print("Please provide the students names and then q to quit")
i=0
while True:
    names : str = input("> ")
    if  names.lower()=="q":
        if i <= 0:
            print("No students were provided")
            names : str = input("")
            continue
        break
    students.update({names : "N"})
    i+=1
while True:
    print("[check] sign ins, [sign] in, or [q]uit:")
    user : str = input("> ")
    match user.lower():
        case "check":
            for i in students:
                print (f"{i}: {students[i]}")
                continue
        case "sign":
            user = input('> ')
            if not user in students:
                print("Student does not exist")
                break
            students[user] = "Y"
            continue
        case "q":
                break
