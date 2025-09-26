print("""Welcome to Count your Blessings!
""")

blessings = [
]

while True:
    options : str = input("[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: ")
    if options.lower()== "add":
        print()
        options= input("Enter something you are thankful for: ")
        blessings.append(options)
        print()
        continue
    elif options.lower() == "remove":
        print()
        options = input('Which item would you like to delete? ')
        if options in blessings:
            blessings.remove(options)
            print()
            continue
        else:
            print("This item is not in your Thankful Box!")
            print()
            continue
    elif options.lower() == "update":
        print()
        options = input("Which item would you like to update? ")
        ind : int = 0
        for i in blessings:
            if i == options:
                break
            ind += 1
            
        if options in blessings:
            options = input("What would you like to change it to? ")
            blessings[ind] = options
            
            print()
            continue
        else:
            print("This item is not in your Thankful Box!")
            continue
    elif options.lower() == "view":
        print()
        print(f'You are thankful for the following {len(blessings)} item(s):')
        ind : int = 1
        for i in blessings:
            print(f'{ind}. {i}')
            ind += 1
        print()
        continue
    elif options.lower() == "q":
        break
    else:
        print("invalid input")
        print()
        continue