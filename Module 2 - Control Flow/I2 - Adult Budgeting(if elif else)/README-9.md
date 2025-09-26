# Control Flow - Intro 2: Adult Budgeting

## Objectives

By the end of this assignment you should be able to:

- understand if, else, and elif statements are and how they are used to control the flow of a program based on conditions.
- understand the syntax for using if, else, and elif statements correctly.
- create and use boolean expressions for conditional checks.

## Resources

### Related Textbook Sections

- Chapter 5 - Choosing Which Statements to Execute (page 86)

### Related Videos

## Assignment

In this exercise, your task is to develop a budget management program. This program will prompt the user to input their monthly income and various expenses. It will then calculate the total expenses and the remaining balance. Using conditional statements, the program will provide feedback on whether the user is staying within their budget or exceeding it.

Your program should run exactly like the examples below. Be sure to run the tests to make sure that your answer is correct.

### Example

```console
--- Budget Manager ---

Enter your monthly income: $2300
Enter your monthly rent: $1100
Enter your monthly utilities: $250
Enter your monthly groceries: $300
Enter other monthly expenses: $200

Your budget is in good shape! You have $450.00 left for the month.
```

```console
--- Budget Manager ---

Enter your monthly income: $1950
Enter your monthly rent: $900
Enter your monthly utilities: $200
Enter your monthly groceries: $350
Enter other monthly expenses: $500

You are breaking even this month. Try to save some money or reduce expenses.
```

```console
--- Budget Manager ---

Enter your monthly income: $1200
Enter your monthly rent: $700
Enter your monthly utilities: $150
Enter your monthly groceries: $300
Enter other monthly expenses: $100

You're over budget by $50.00. Consider reducing some expenses or finding additional income sources.
```

### Common Misconceptions/Errors to Watch Out For

- **elif** and **else** are not required; you can use only **if** if needed.
- Only the first true condition in if/elif blocks is executed; the rest are skipped.
- Proper indentation is crucial as Python uses it to define code blocks.
- **else** executes only if all previous conditions are false; if omitted, nothing happens when conditions are false.

### Rubric/Style Guide

- [ ] Ask a user for their income.
- [ ] Ask a user for their various expenses.
- [ ] You should use a single set of related branches(if, elif, else).
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
