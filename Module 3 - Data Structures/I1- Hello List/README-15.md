# Intro 1: Hello List
In this exercise you will create a small C.R.U.D app to help users practice thankfulness. Your application should repeatedly prompt the user to enter, remove, view, or update things they are thankful for.

Example:
```
Welcome to Count your Blessings!

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: Add

Enter something you are thankful for: Video Games

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: Add

Enter something you are thankful for: Homework

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: View

You are thankful for the following 2 item(s):
1. Video Games
2. Homework

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: Remove

Which item would you like to delete? Video Gam
This item is not in your Thankful Box!

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: Remove

Which item would you like to delete? Homework

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: View

You are thankful for the following 1 item(s):
1. Video Games

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: quit
invalid input

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit:
```


### Lists - Key Concepts/Misconceptions
- You may hear lists referred to as ‘arrays’ in other programming languages.  There are small differences but at this stage we will treat them as essentially the same thing.
- A list can store multiple items of data.
- Items in a list are surrounded by square brackets.  Each item is separated by a comma.
- Lists are indexed - each item is given a numerical position in the list.
- Lists are named in the same way as variables - the programmer decides what they are called.  Using camel case is best practice
- Indexing starts at 0, students often forget this as they are in the habit of starting to count with 1.
- A list is changeable - each individual item can be edited, added or removed. Extra items can be added to the list.
- A list allows duplicate items.

### Related Videos

- [Data - Hello Lists](https://www.youtube.com/watch?v=GeAKnX7XOxo&list=PL6xuclUa80QihnQkyfqfPl21Fh6AjT9eT&index=3)

### Related Textbook Sections
- Chapter 8 - Storing and Accessing Data in Lists (page 130)
- Chapter 8 - The Empty List (page 132)
- Chapter 8 - Type Annotations for Lists (page 133)
- Chapter 8 - Operations on Lists (page 135)
- Chapter 8 - List Methods (page 141)
- Chapter 9 - Processing Items in a List (page 149)

### Rubric

- [ ] You must use a single list
- [ ] Display the welome message
- [ ] Collect "blessings" from the user
- [ ] Display how many things they entered and repeat the provided blessings back to them.
- [ ] Allow the user to add their "blessings"
- [ ] Allow the user to view their "blessings"
- [ ] Allow the user to updates their "blessings"
- [ ] Allow the user to deletes their "blessings"
- [ ] Consider invalid inputs and items not in a list

### Style Guide
- [ ] Appropriate and meaningful comments
- [ ] Code should be formatted neatly.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
