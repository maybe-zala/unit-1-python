# Control Flow - Intro 1: The Moment of Truth

## Objectives

By the end of this assignment you should be able to:

- understand what Boolean values are (True and False) and how they are used in Python programming.
- understand comparison operators (==, !=, >, <, >=, <=) to compare values and generate Boolean results.
- use of logical operators (and, or, not) to combine or negate Boolean expressions.

## Resources

### Related Videos

## Assignment

"The Moment of Truth" is an American game show where contestants answer 21 increasingly personal and potentially embarrassing questions truthfully to win cash prizes. In our version, we will replace these personal questions with 21 mathematical questions. Contestants must provide "true" or "false" answers to these questions to win their rewards.

The producers want to ensure that the correct answers are used for the predefined mathematical questions. Your task is to develop a program that prompts the user to enter a number and then performs comparisons between the user-provided number and a predefined value. The program should return "true" or "false" based on whether the user’s input meets the comparison criteria. Also, ensure that your program operates and appears exactly as demonstrated in the examples, and maintains the same sequence of comparisons.

### Example

```console
***************************************
*                                     *
*   Welcome to the Moment of Truth!   *
*                                     *
***************************************

Get ready for an exciting challenge where your decisions matter!
Make the right choices, and you might just find out what truth lies ahead.

Good luck and enjoy the game!

Please enter a number: 5

1. Is the number 5 less than 100?  True
2. Is the number 5 greater than 75?  False
3. Is the number 5 equal to 13?  False
4. Is the number 5 not equal to 18?  True
5. Is the number 5 less than or equal to 8?  True
6. Is the number 5 greater than or equal to 15?  False
7. Is the number 5 equal to 2 + 2?  False
8. Is the number 5 less than 2^5?  True
9. Is the number 5 equal to 30% of 20?  False
10. Is the number 5 divisible by 3  False
11. Is the number 5 less than 25?  True
12. Is the number 5 greater than 103?  False
13. Is the number 5 equal to 67?  False
14. Is the number 5 divisible by 5?  True
15. Is the number 5 less than or equal to 23?  True
16. Is the number 5 not equal to 15?  True
17. Is the number 5 equal to 7 * 5?  False
18. Is the number 5 less than 10?  True
19. Is the number 5 equal to 15% of 50?  False
20. Is the number 5 divisible by 8?  False
21. Is the number 5 divisible by 7?  False
```

```console
***************************************
*                                     *
*   Welcome to the Moment of Truth!   *
*                                     *
***************************************

Get ready for an exciting challenge where your decisions matter!
Make the right choices, and you might just find out what truth lies ahead.

Good luck and enjoy the game!

Please enter a number: 9

1. Is the number 9 less than 100?  True
2. Is the number 9 greater than 75?  False
3. Is the number 9 equal to 13?  False
4. Is the number 9 not equal to 18?  True
5. Is the number 9 less than or equal to 8?  False
6. Is the number 9 greater than or equal to 15?  False
7. Is the number 9 equal to 2 + 2?  False
8. Is the number 9 less than 2^5?  True
9. Is the number 9 equal to 30% of 20?  False
10. Is the number 9 divisible by 3  True
11. Is the number 9 less than 25?  True
12. Is the number 9 greater than 103?  False
13. Is the number 9 equal to 67?  False
14. Is the number 9 divisible by 5?  False
15. Is the number 9 less than or equal to 23?  True
16. Is the number 9 not equal to 15?  True
17. Is the number 9 equal to 7 * 5?  False
18. Is the number 9 less than 8?  False
19. Is the number 9 equal to 15% of 50?  False
20. Is the number 9 divisible by 8?  False
21. Is the number 9 divisible by 7?  False
```

### Common Misconceptions/Errors to Watch Out For

- Booleans vs. Integers: True and False are distinct from 1 and 0, though they are often used similarly in numeric contexts.
- Boolean Expression Results: Ensure expressions are correctly formulated to avoid unexpected results, as they evaluate to True or False.
- == vs. =: Use == for comparison and = for assignment to avoid errors.
- Non-Zero Values: Non-zero values are considered True, but 0 and None are False.
- is vs. ==: Use == for comparing values and is for comparing object identity.
- Empty Containers: Remember that empty strings and lists are considered False.
- Logical Operators Misuse: Use parentheses to clarify logical expressions and ensure correct operator usage.

### Rubric/Style Guide

- [ ] Ask the user to enter a number
- [ ] Display the question
- [ ] True and False should NOT be printed as a string.
- [ ] True and False must be displayed using expressions
- [ ] All test cases are passed.
