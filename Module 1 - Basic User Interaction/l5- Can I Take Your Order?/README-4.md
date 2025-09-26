# Basic User Interaction - Intro 5: Can I Take Your Order?

## Objectives

By the end of this assignment you should be able to:

* Format strings through various techniques

## Resources
[Python Formatting](https://www.youtube.com/watch?v=FrvBwdAU2dQ)

## Assignment

For this exercise, you'll create a checkout program for the popular [Good Burger](https://en.wikipedia.org/wiki/Good_Burger) fast food chain. Your program will prompt the user to specify the number of Good Burgers, French fries, and drinks they wish to buy. Based on their input, the program will generate and display a receipt.

### Example 

```console
Welcome to Good Burger.
Home of the Good Burger.
Can I take your order?

Good Burgers ($4.50): 2
French Fries ($1.50): 3
Drinks       ($1.00): 4

Here is your receipt:
- Good Burgers $4.50 x 2 = $9.00
- French Fries $1.50 x 3 = $4.50
- Drinks       $1.00 x 4 = $4.00
TOTAL = $17.50
```

```console
Welcome to Good Burger.
Home of the Good Burger.
Can I take your order?

Good Burgers ($4.50): 1
French Fries ($1.50): 1
Drinks       ($1.00): 1

Here is your receipt:
- Good Burgers $4.50 x 1 = $4.50
- French Fries $1.50 x 1 = $1.50
- Drinks       $1.00 x 1 = $1.00
TOTAL = $7.00
```

### Common Misconceptions/Errors to Watch Out For

* Outdated Formatting Methods:
  * Avoid using % formatting, and prefer str.format() or f-strings for modern code.
* Type Conversion:
  * Convert non-string types to strings before concatenation to avoid TypeError.
* Format Specifiers:
  * Use correct format specifiers (%d for integers, %f for floats, etc.) to match data types.
* Placeholder Usage:
  * Ensure braces {} are used properly with str.format() to avoid errors.
* Indexing in str.format():
  * Use positional or keyword arguments correctly to prevent confusion.
* F-Strings:
  * Make sure to use Python 3.6 or later for f-strings; they won’t work in earlier versions.
* Special Characters:
  * Escape curly braces in f-strings by using double braces ({{ and }}).
* Padding and Alignment:
  * Use padding and alignment options to format output neatly.

### Rubric/Style Guide
* [ ] Displays the welcome message
* [ ] Get the quanity of items from the user
* [ ] Calculate and display the price of each item.
* [ ] Calculate and display the total all items
* [ ] Must format like the output provided.
* [ ] Variables should have meaningful names that accurately describe what they refer to.
* [ ] Must pass all test cases.