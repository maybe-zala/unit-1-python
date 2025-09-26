# Intro 2: More Bad Sports

In this exercise, I've given you a complete solution to the original Bad Sports. Your job is to extract four helper functions that correctly implements the logic for the following functions:

- `is_on_team`
    - 1 argument for the name of a person
    - returns a boolean to indicate whether or not the provided name is for a person on the team.
- `rick_shakes`
    - 2 arguments
        - One for the name of a person
        - One for whether or not the person's team won
    - returns a boolean to indicate whether or not Rick shakes hands
- `john_shakes`
    - 2 arguments
        - One for the name of a person
        - One for whether or not the person's team won
    - returns a boolean to indicate whether or not John shakes hands
- `jared_shakes`
    - 2 arguments
        - One for the name of a person
        - One for whether or not the= person's team won
    - returns a boolean to indicate whether or not Jared shakes hands

**Important Note:** Your functions should be defined at the top of the file. Your application logic should be behind a `if __name__ == '__main__':` branch. If you don't move your application logic behind this branch, it will cause your tests to time out because it is waiting on user input.

## Examples

```
Name: Nick
Did you win? Yes
Rick: *shakes hand*
John: ...
Jared: ...
```

```
Name: Maureen
Did you win? No
Rick: *shakes hand*
John: ...
Jared: *shakes hand*
```

```
Name: Joe
You weren't even on the team!
```

### Rubric

- [ ] Ask the user for their name
- [ ] Ask the user if they won
- [ ] For each member of the other team, print out whether or not they shook hands
  - [ ] If the user won, Rick refuses to shake hands with Carol and Maureen.
  - [ ] If the user lost, Rick refuses to shake hands with Nick. 
  - [ ] If the user won, John refuses to shake hands with Nick.
  - [ ] If the user lost, John refuses to shake hands with Carol and Maureen.
  - [ ] Jared refuses to shake hands with Nick.
- [ ] Prints "You weren't even on the team!" if the user inputs a name that isn't apart of your team.
- [ ] Helper functions extracted and implemented correctly.
    - They should not print or take input. They should only return the correct value for the provided arguments. It is up to your main function to use these functions correctly and print/input as necessary.
- [ ] Functions defined at the top of the file with the "main" function below the other functions.
- [ ] Application logic is inside `if __name__ == '__main__':` branch.
- [ ] You need to add type annotations for your functions.

### Style Guide
- [ ] Appropriate and meaningful comments
- [ ] Code should be formatted neatly.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.