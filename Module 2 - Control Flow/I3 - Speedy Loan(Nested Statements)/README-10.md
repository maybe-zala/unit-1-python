# Control Flow - Intro 3: Speedy Loans

## Objectives

By the end of this assignment you should be able to: 

- learn what nested if, elif, and else statements are and how they function within other conditional statements.
- be able to correctly write and indent nested conditional statements.

## Resources

### Related Textbook Sections

### Related Videos

## Assignment

You have been hired by Speedy Loans to develop a loan decision-making system. Your job is to create a program that asks
the user a series of questions to assess whether their loan application should be approved. A flowchart has been provided
to guide you through the decision-making process.

### Example

```console
--- Speedy Loans ---

Income Level (High, Medium or Low): High
Yes
```

```console
--- Speedy Loans ---

Income Level (High, Medium or Low): Medium
Credit Score(High or Low): Low
Employment Type(Self or Salaried): Self
No
```

### Common Misconceptions/Errors to Watch Out For

- **elif** and **else** are not required; you can use only **if** if needed.
- Only the first true condition in if/elif blocks is executed; the rest are skipped.
- Proper indentation is crucial as Python uses it to define code blocks.
- **else** executes only if all previous conditions are false; if omitted, nothing happens when conditions are false.

### Rubric/Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Must have comments
- [ ] Test Case must pass
