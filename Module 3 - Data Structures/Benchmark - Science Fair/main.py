projects = {}
while True:
    option = input('[project] or [done]> ')
    if option.lower() == "project":
        title = input("Title: ")
        student_name = input("Student Name: ")
        description = input('Description: ')
        projects[title] = {'Student Name': student_name, "Description": description, 'num_vote': 0 }
    elif option.lower() == 'done':
        if len(projects) == 0:
            print("No projects were provided.")
            break
        else:
            while True:
                choice = input("[vote] or [done]> ")
                if choice == 'vote':
                    user_vote = input('Which project (title)? ')
                    projects[user_vote]['num_vote']  += 1
    

                    pass
                elif choice.lower() == 'done':
                    winner = 0x
                    for key in projects:
                        if projects[key]['num_vote'] > winner:
                                winner = projects[key]['num_vote']
                    for x in projects:
                        if projects[x]['num_vote'] == winner:
                            print(f'{x} is the winner!')
                    quit()
                else:
                    print('Invalid Input')
    else:
        print('Invalid Input')
