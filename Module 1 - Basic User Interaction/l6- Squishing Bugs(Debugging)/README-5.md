# Basic User Interaction - I6: Squishing Bugs

## Objectives

By the end of this assignment you should be able to:

- understand the importance of user interaction in programming and its role in creating interactive applications.
- understand how user input and output facilitate communication between the user and the program.
- use the input() function to collect user input.

## Resources

- [15 Common Errors in Python and How to Fix Them](https://betterstack.com/community/guides/scaling-python/python-errors/#1-syntaxerror)
- [Writing Comments in Python (Guide)](https://realpython.com/python-comments-guide/)

### Related Videos

- [Python Comments - All You Need To Know (And Stuff You Didn't!)](https://www.youtube.com/watch?v=ZgAcB8HiQmo)
- [Python Error Types](https://www.youtube.com/watch?v=Kf6dvup_6Mo)

### Common Misconceptions/Errors to Watch Out For

- Syntax Errors: Missing or misplaced punctuation, like colons or parentheses.
- Indentation Errors: Inconsistent use of tabs and spaces or incorrect indentation levels.
- Name Errors: Using variables before they are defined.
- Type Errors: Performing operations on incompatible data types.
- Index Errors: Accessing list or string indices that are out of range.
- Key Errors: Accessing non-existent dictionary keys.
- Attribute Errors: Calling methods or attributes that don’t exist for a data type.
- ZeroDivisionError: Dividing a number by zero.
- FileNotFoundError: Trying to open a file that doesn’t exist.
- Import Errors: Importing modules or packages that are not found or incorrectly named.
  
### Debugging Tips

- Use Print Statements: Print intermediate values to track down issues.
- Leverage Debuggers: Use tools like pdb or IDE debuggers for step-by-step execution.
- Read Tracebacks: Tracebacks provide useful information about where errors occur.
- Write Tests: Unit tests help catch errors early and ensure code behaves as expected.
  
## Assignment

Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price. It consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud. The game is frequently played as a party game or as a pastime. The goal of this lesson is to introduce you to debugging. You are provided a program with some of the most common programming errors. Your job will be to correct all errors. Throughout your time at base camp you will encounter many syntax and logical errors that may frustrate you. However, with practice you will be able to detect and correct your errors.  

Review and edit the provided code to correct all **bugs**.

**Note** The code may contain both logical and syntax errors. Syntax errors will generate error messages and prevent the code from running. Logical errors do not produce error messages but can lead to incorrect results or unexpected behavior. To ensure the code functions as intended, it is crucial to correct both types of errors. Additionally, you should improve the readability of the code and add comments to explain each step can make it easier to understand and maintain.

Step 1: Multiply the number the user inputed by 3 and save it to a variable called day.
Step 2: Do 12.65 to the power of 3 rounded to the nearest whole number and save it to a variable called year.
Step 3: Ask the user enter a name and store it in a variable called first_name.
Step 4: Ask the user enter an adjective and store it in a variable called adjective.
Step 5: Ask the user to enter a type of bird and store it in a variable called type_of_bird.
Step 6: Store the past tense of the verb run to a variable called verb_past_tense.
Step 7: Subtract 23 from 57 and save it to a variable called num_of_stairs.
Step 8: Save 0.33 to a variable called amount_1, and save 24.25 to a variable called amount_2. Multiply amount_1 with amount_2 and save the result to a variable called ounces rounded to the hundreth place.
Step 9: Ask the user to enter a price and store it in a variable called monthly_price. **Please account for cents in the price.**
Step 10: Multiply monthly_price by 12 and subtract 10 and store it in a varaible called yearly_price which should be rounded to the nearest hundredth place.

## Example

```console
Enter a number between 1 - 10: 2
Enter a name: Sam
Enter an adjective: strong
Enter a type of bird: turkey
Enter a price: $2.35

It was November 6, 2024, Sam woke up to the strong smell of turkey roasting in the kitchen downstairs. They ran down 
the 34 stairs to see if they could help with dinner. Their mom said, 'See if your father needs a fresh drink.' So they carried a tray of 8.0 oz 
glasses full of lemonade into the living room. When they got there, they couldn't believe their eyes! To finish this story please subscribe for the low 
monthly price of $2.35 or for even more savings our yearly price of $18.20.
```

### Rubric/Style Guide

**Important** Not only should you pass all test but you must also follow the rubric and style guide.

- [ ] Add useful comments
- [ ] Correct all logical errors
- [ ] Correct all syntax errors
- [ ] Abide by naming conventions
- [ ] All test cases are passed
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] Code should include comments however, no sloppy/unnecessary/commented out code.
