# Control Flow - Intro 4: For Loops

## Objectives

By the end of this assignment you should be able to:

- Learn how to repeatedly execute blocks of code using loops.
- Be able to modify the flow of execution within loops.

## Resources

[Python `for` Loops Tutorial – YouTube](https://www.youtube.com/watch?v=KWgYha0clzw)

## Assignment

### Task 1: 
You will write a Python program that asks the user to enter a string, and then counts how many vowels (a, e, i, o, u) are in that string. The program should work regardless of uppercase or lowercase letters.

#### Steps to Count Vowels in a String

1. **Prompt the user** to enter a string using `input()`.

2. **Define a variable** to store the count of vowels. Start it at `0`.

3. **Create a `for` loop** that goes through each character in the string.

4. **Inside the loop:**
   - Convert each character to lowercase using `.lower()`.
   - Check if the character is one of the vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`).
   - If it is, increase your vowel count by `1`.

5. **After the loop ends**, print the total number of vowels.

### Task 2: 
#### Steps to create a diamond

1. **Prompt the user** to enter the number of rows for the diamond.
   - This value controls the height of the top half of the diamond.
   - Use `input()` and convert it to an integer with `int()`.

2. **Print the upper part of the diamond (pyramid):**
   - Use a `for` loop that goes from `1` to `num_rows` (inclusive).
   - For each row:
     - Print spaces to center the stars: `' ' * (num_rows - i)`
     - Then print stars to form the row: `'*' * (2 * i - 1)`

3. **Print the lower part of the diamond (inverted pyramid):**
   - Use another `for` loop that goes from `num_rows - 1` down to `1`.
   - For each row:
     - Print spaces: `' ' * (num_rows - i)`
     - Then print stars: `'*' * (2 * i - 1)`
### Example
![Example](example.png)

### Common Misconceptions/Errors to Watch Out For

- Incorrect indentation inside the loop block
- Modifying a list while iterating over it
- Using range(len(...)) unnecessarily
- Off-by-one errors with range() due to misunderstanding its exclusive upper bound
- Incorrect use of break or continue
- Looping over the wrong variable or data source
- Forgetting to convert input to the correct data type
- Unintentionally reusing the loop variable elsewhere in the code
- Incorrect range() arguments that prevent the loop from running or cause logic errors
- Confusing for loops with while loops in the wrong context

### Rubric/Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
