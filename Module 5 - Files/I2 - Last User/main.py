def main():
    import os
    while True:
        name = input("Name? ")
        if os.path.getsize('work.txt')== 0:
            print("You are the first user!")
        
        else:
            with open("work.txt", "r") as work_file:
                contents = work_file.read()
                print(f'{contents} was the last user of this program.')
                work_file.close

        with open("work.txt", "w") as work_file:
            work_file.write(name)
    
if __name__ == '__main__':
    main()