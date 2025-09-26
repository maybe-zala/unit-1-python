# I4 Dictionary: 📖 Book Author Lookup Program

## 🎯 Objectives

- Understand how to use **Python dictionaries** to map keys to values.
- Learn to build a simple **text-based menu** interface.
- Practice using **loops** and **conditional logic** for user interaction.
- Apply dictionary operations to retrieve and display values based on user input.

---

## 📚 Resources

### 🎥 Related Videos
- [Keys Vs Values Vs Items](https://www.youtube.com/watch?v=_3wM_-UKCz0&list=PL6xuclUa80Qhn2Roxw9RPmDEatrJdg09S&index=2)
- [Typing Dicts](https://www.youtube.com/watch?v=k4jZtRYmd7Q&list=PL6xuclUa80Qhn2Roxw9RPmDEatrJdg09S&index=3)

### 📖 Related Documentation

- [Real Python – Dictionaries in Python](https://realpython.com/python-dicts/)
- [Python Docs – Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

---

## 📝 Assignment

In this exercise, you'll write a Python program that helps users find out who authored a requested book. You are provided a 
dictionary with the book information.

Your program should:
Allow the user to type commands to:
   - View the list of books.
   - Enter the name of a book to see the author.
   - Exit the program.

### User Commands:
- `books`: Show the list of available books.
- `author`: Prompt for a book title, then show the author.
- `quit`: Exit the program.

Use a loop to keep prompting the user until they choose to quit.

---

## 🧪 Example of the Solution Output
```console
view [books], show [author], [quit]> books
- Harry Potter
- Effective Testing with RSpec 3
- Automate the Boring Stuff
- Quiet
- Peak
view [books], show [author], [quit]> author
book> Harry Potter
JK Rowling
view [books], show [author], [quit]> author
book> Automate the Boring Stuff
Al Sweigart
view [books], show [author], [quit]> quit
```

---

## ⚠️ Common Misconception

- **Incorrect key matching**: Users may type a book title with different capitalization or spelling than what’s stored in the dictionary.  
  → Tip: You can either enforce exact matches or use `.lower()` to make the comparison case-insensitive.

- **Wrong data structure**: Some students mistakenly use a list of tuples or two separate lists instead of a dictionary, which complicates lookup.  
  → Tip: A dictionary is the most efficient way to map book titles to authors.

---

## ✅ Rubric

- [ ] The user can view the list of known books.
- [ ] The user can view the author of a specific book.
- [ ] The user can quit the program gracefully.
- [ ] Dictionary is used to store book-author pairs.

---

## 🎨 Style Guide

- [ ] Include **comments** explaining each section of the code.
- [ ] Code should be **formatted neatly** and consistently (indentation, spacing).
- [ ] Variables must have **meaningful names** that accurately describe their contents.
- [ ] Avoid **sloppy**, **unnecessary**, or **commented-out** code.
