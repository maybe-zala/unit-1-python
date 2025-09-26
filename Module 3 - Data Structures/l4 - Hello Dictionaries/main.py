from typing import Dict

book_authors = {
    'Harry Potter': 'JK Rowling',
    'Effective Testing with RSpec 3': 'Myron Marston',
    'Automate the Boring Stuff': 'Al Sweigart',
    'Quiet': 'Susan Cain',
    'Peak': 'Anders Ericsson',
}


while True:
    options = input("view [books], show [author], [quit]> ")
    if options.lower() == "books":
        for x in book_authors:
            print(f"{x}")
        continue
    elif options.lower() == "author":
        options = input("book> ")
        print(book_authors[options])
    elif options.lower() == "quit":
        break
    else:
        print('Invalid input')
