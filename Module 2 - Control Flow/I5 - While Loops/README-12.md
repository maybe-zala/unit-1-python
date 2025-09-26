# Control Flow - I5: While Loops

## Objectives

By the end of this assignment you should be able to:

- Use while loops to repeat code based on a condition.
- Write and update loop conditions correctly to avoid infinite loops.
- Control loop flow with break, continue, and loop variables.

## Resources

[Python `While` Loops Tutorial – YouTube](https://www.youtube.com/watch?v=rRTjPnVooxE)

## Assignment
For this exercise you will build a program that sorts and totals a collection of coins. You get this collection of coins from your user as a string where each letter corresponds to a coin. For example, Each `P` represents a penny. Your job is to loop over the string and count the coins. Your program should display all the coin counts as well as the total amount of money. Also, you will include some error validation. If the user include a letter that does not represent a coin that letter should be ignored and a warning message should appear like in the example.

### Example

```
Coins: PPNPNNDQDP

Coin Summary:
Pennies (P): 4
Nickels (N): 3
Dimes (D): 2
Quarters (Q): 1
Total: $0.64
```
```
Coins: DDGPPP

Warning: Unknown coin type 'G' ignored.
Coin Summary:
Pennies (P): 3
Nickels (N): 0
Dimes (D): 2
Quarters (Q): 0
Total: $0.23
```

### Common Misconceptions/Errors to Watch Out For
- Creating an infinite loop unintentionally
- Using the wrong loop condition
- Off-by-one errors in loop boundaries
- Using = instead of == in the condition
- Modifying the loop variable incorrectly or inconsistently
- Forgetting to update the loop variable
- Misusing continue, causing skipped updates or infinite loops
- Not using break when necessary to exit the loop
- Resource mismanagement (e.g., not closing files or connections)
- Overcomplicating logic that could be handled with a for loop

### Rubric/Style Guide

- [ ] Uses a single `while` loop.
- [ ] Asks the user for the coins.
- [ ] Displays amount of each coin type.
- [ ] Displays the total amount of money.
- [ ] Display warning message for each ignored coin
- [ ] Appropriate and meaningful comments
- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.