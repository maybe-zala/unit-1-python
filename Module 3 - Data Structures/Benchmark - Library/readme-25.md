# Benchmark: Library

In this benchmark, your job is to implement a library management system. The library should manage a collection of books. The user should be able to add a new book to the library, view the books in the library, lend a book, and return a book. Your program must keep track of each book's title, author(s), and who is borrowing it (if anyone is borrowing it).

Example:

```
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> book
Title?
> How To Design Programs
Author(s)?
> Felleisen et al
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> book
Title?
> Structure and Intepretation of Computer Programs
Author(s)?
> Abelson and Sussman
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> view
1. [Available] How to Design Programs by Felleisen et al
2. [Available] Structure and Intepretation of Computer Programs by Abelson and Sussman
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> loan
Which book?
1. How to Design Programs by Felleisen et al
2. Structure and Intepretation of Computer Programs by Abelson and Sussman
> 2
Borrower's name?
> Nate
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> view
1. [Available] How to Design Programs by Felleisen et al
2. [Unavailable] Structure and Intepretation of Computer Programs by Abelson and Sussman
> loan
Which book?
1. How to Design Programs by Felleisen et al
> 1
Borrower's name?
> Etan
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> return
Title?
> Structure and Intepretation of Computer Programs
Borrower's Name?
> Nate
> view
1. [Unavailable] How to Design Programs by Felleisen et al
2. [Available] Structure and Intepretation of Computer Programs by Abelson and Sussman
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> quit
```


### Rubric

- [ ] Users can add books to the library
- [ ] Users can view the library's inventory
    - Viewing the inventory shows each book's title, author, and availability.
- [ ] Users can loan out books
    - A book can not be loaned out again without being returned first. 
- [ ] Users can return books
    - A book can only be returned by the borrowing user.
- [ ] Users can quit

### Style Guide

- [ ] Code should be formatted neatly.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.