# Basic User Interaction - Project 1: Coffee Shop Simulator

## Objectives

By the end of this assignment you should be able to:

* Understand what a variable is.
* Assign variables and print variables.
* Explain rules for naming variables.
* Apply Python’s rules for naming variables

## Resources

### Related Videos

* [Reserved Words](https://docs.google.com/document/d/1NG3x8Q8T7RCPG1-9Di_BDPbtVckOdDgACbPXhAJqo20/edit?usp=sharing)
* [LEGAL VARIABLES](LEGAL_VARIABLES.md)
* [NAMING_CONVENTION](NAMING_CONVENTION.md)

## Assignment

We have now gathered enough beans of wisdom to pour our first cup in the Base Camp Coffee Shop application. Since this is our first step in writing our app, we'll keep things simple and use what we've learned so far to set up the parameters. Your task is to create a new file and save it as `coffee.py` and create a Coffee Shop application that will ask for the users name, the users coffee shop name, and ask for how much each cup should cost. It should output just like the demo below.

### Example

```console
☕ Base Camp Coffee Shop Simulator 4000, Version 1.00 ☕
Copyright (C) 2024 BaseCamp Media, All Rights Reserved.

Let's collect some information before we start the game.

What is your name? Brittany
What do you want to name your coffee shop? Magnolia Coffee

Thanks, Brittany. Let's set some initial pricing.

What do you want to charge per cup of coffee? 1.00

Great. Here's what we've collected so far.

Your name is Brittany and you're opening Magnolia Coffee!
Your first cup of coffee will sell for $1.00.
```

### Common Misconceptions/Errors to Watch Out For

* Python requires variables to be initialized before use. Using an uninitialized variable results in a NameError.
* Python = is used for assignment (e.g., x = 10), whereas == is used for comparison (e.g., x == 10).
* Naming variables after built-in functions or types (e.g., list, str, print) can lead to unexpected behavior or bugs in your code.
* In multiple assignments like a = b = c = 10, all variables are set to reference the same object. Changes to mutable objects affect all variables pointing to that object.
* No two variables can have the same name(**Actually they can which will be discussed later, but as of now just don't do it**).
* Variable names should be meaningful (give you a clue as to the data stored)
* Variable names should follow python's naming convention.
* Variable names cannot contain spaces.

### Rubric/Style Guide

* [ ] Displays the name of the application and the copyright as shown in the output above.
* [ ] Get the users name and shop name.
* [ ] Get the initial price of their coffee.
* [ ] Displays the users name and the name of their coffee shop that they are opening.
* [ ] Display how much the cup of coffee will sell for.
* [ ] Must format like the output provided.
* [ ] Variables should have meaningful names that accurately describe what they refer to.
