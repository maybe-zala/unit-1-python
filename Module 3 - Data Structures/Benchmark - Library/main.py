books = []

while True:
    print('add [book], [view] inventory, [loan] book, [return] book, [quit]?')
    user_choice = input("> ")
    if user_choice == 'book':
        print('Title?')
        title = input("> ")
        print("Author(s)?")
        author = input("> ")
        books.append([title, author, 'Available'])

    elif user_choice == 'view':
        count = 1
        for book in books:
            print(f'{count}. [{book[2]}] {book[0]} by {book[1]}')
            count += 1
    
    elif user_choice == 'loan':
        print("Which book?")
        count = 1
        for book in books:
            if book[2] == 'Available':
                print(f'{count}. {book[0]} by {book[1]}')
                count += 1
        book_choice = int(input("> "))
        print("Borrower's name?")
        borrower = input("> ")
        count=1
        for book in books:
            if book[2] == 'Available':
                if count == book_choice:
                    book[2]= "Unavailable"
                    book.append(borrower)
                count += 1

    elif user_choice == 'return':
        print("Title?")
        book_return = input('> ')
        print("Borrower's Name?")
        return_person = input('> ')
        count = 1
        for book in books:
            if book[0] == book_return:
                book[2] = 'Available'
                count += 1
        count=1
    elif user_choice == 'quit':
        break
    else:
        print('Invalid input.')