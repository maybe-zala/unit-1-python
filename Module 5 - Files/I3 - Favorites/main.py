def main():
    while True:
        options = input("[read], [write], [quit]> ")
        if options == "read":
            favorite = input("Favorite> ")
            items = "favorite {favorite}"
            try:
                with open("favorite "+ favorite, "r") as file:
                    content = file.read()
                    print("Your favorite", favorite,"is", content)
            except FileNotFoundError:
                print(f"You have not saved a favorite {favorite}")
        elif options == "write":
            fav = input('Favorite> ')
            item = input(f'Favorite {fav}> ')
            with open("favorite "+fav, "w") as file:
                file.write(item)
                print(f'Wrote {item} as favorite {fav}.')
        elif options == "quit":
            break
        else:
            print("Invalid Input")
        
if __name__ == '__main__':
    main()