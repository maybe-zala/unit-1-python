def main():

    name= input("Please enter your name: ")

    with open("dry-erase-board.txt", 'a') as f:
        f.write(f'{name} wuz here')

if __name__ == '__main__': main()