# File Handling - Intro 2: Last User

In this exercise, you will write a program that remembers the last user to run the program.

You should display the last user, ask the current user for their name, and save that name to the file. If there is no previous user, you should print a message indicating the current user is the first user of this program.

```
$ python3 main.py
You are the first user of this program!
Name? Brittany
$ python3 main.py
Brittany was the last user of this program.
Name? Sean
$ python3 main.py
Sean was the last user of this program.
Name? Janet
```

## Related Textbook Sections

- Chapter 10 - Opening a File (page 173)
- Chapter 10 - Writing Files (page 182)

## Rubric

- [ ] Show the user the name of the last person to use the program.
    - If they are the first user, show that.
- [ ] Ask the for their name
- [ ] Save that they are the new last user.

## Style Guide
- [ ] Must include comments
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.