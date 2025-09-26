Persistence - Intro 4: Many Previous Users

In this exercise, you will write a program very similar to the "Last User" program from intro exercise 2. Unlike it, this program will remember all previous users. To do so, you will append to the file instead of overwriting it. Additionally, you will read a list of all past users from the file instead of reading just the last user.

$ python3 main.py
You are the first user of this program!
Name? Nate
$ python3 main.py
1 user has run this program.
Nate was the last user of this program.
Name? Evil Nate
$ python3 main.py
2 users have run this program.
Evil Nate was the last user of this program.
Name? Janet
Related Videos

Persistence - Files With Many Entries
Persistence - Appending vs Writing Files
Related Textbook Sections

Chapter 10 - Techniques for Reading Files (page 176)
Chapter 10 - Writing Files (page 182)
Rubric

 Display how many users have run the program previously
 Display the name of the last user
 Ask them for their names
 Save that they have used the program
Style Guide

 Code should be formatted with black.
 Variables should have meaningful names that accurately describe what they refer to.
 No sloppy/unnecessary/commented out code.
 Functions defined at the top of the file
 Application is implemented inside main function that is called inside if __name__ == '__main__':.
 Input is collected with input helper functions.
 Input helpers use validation functions that don't contain side effects and are tested thoroughly.
 Any significant pure logic is extracted and tested thoroughly.
 All functions have type annotations and pass the type checker.