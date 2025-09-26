password : int = -1

while True:
    if password == -1:
        user_password : int= input('What is the passcode? ')
        password = user_password
    user_input : str = input("[enter], [change] passcode, [quit]> ")
    if user_input == 'enter':
        user_password: int= input("What is the passcode? ")
        if user_password == password:
           print("You can enter.")
           continue
        else:
            print("Wrong passcode.")
            continue
    elif user_input == "change":
        user_password : int =input("What is the passcode? ")
        if user_password == password:
            user_password : int = input("What should the new passcode be? ")
            password = user_password
            continue
        else:
             print("Wrong passcode.")
             continue
    elif user_input== "quit":
        break
    else:
        print("Invalid entry.")