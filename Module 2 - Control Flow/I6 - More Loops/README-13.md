# I6: Can I Take Your Order? [Redux]


## Resources
- [Input Validation Loops](https://www.youtube.com/watch?v=LUWyA3m_-r0)
- [Common Input Validation Loops](https://www.youtube.com/watch?v=eF5mObNHeek)
- Chapter 9 - Controlling Loops Using break and continue (page 77)

## Assignment
For this exercise you are going to reimplement 'Can I Take Your Order?', but with input validation. Specifically, someone should not be allowed to ask for negative number of burgers, fries, or drinks. They should also have to give you a number.

## Example
```
Welcome to Good Burger.
Home of the Good Burger.
Can I take your order?

Good Burgers ($4.50): -2
Quantity must be a positive number.
Good Burgers ($4.50): 2
French Fries ($1.50): 3
Drinks       ($1.00): apples
Quantity must be a positive number.
Drinks       ($1.00): 4

Here is your reciept:
- Good Burgers $4.50 x 2 = $9.00
- French Fries $1.50 x 3 = $4.50
- Drinks       $1.00 x 4 = $4.00
TOTAL = $17.50
```

## Rubric/Style Guide

- [ ] Displays error message and repeats prompt if the user provides an invalid quantity.
- [ ] Ask the user for how many burgers, fries, and drinks they want
- [ ] Display a receipt with:
  - [ ] Each item's quantity and subtotal
  - [ ] Order total
- [ ] Appropriate and meaniful comments
- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.