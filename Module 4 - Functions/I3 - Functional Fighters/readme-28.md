# Functions - Intro 3: Functional Fighter

In this exercise, your job is to refactor the provided starter code by extracting the functions defined below.).

Required Functions:

- `input_pokemon_type`
    - No arguments
    - Repeatedly asks the user for a pokemon type until they respond with a valid pokemon type.
    - Returns the valid pokemon type entered by the user.

- `random_pokemon_type`
    - No arguments
    - Returns a random, valid pokemon type for this game.


### Related Textbook Sections

- Chapter 3 - Using Local Variables for Temporary Storage (page 39)
- Chapter 3 - Tracing Function Calls in the Memory Model (page 40)

### Rubric

**Note:** This exercise doesn't have test cases. I can't write reliable test cases because something different should happen every time even if the inputs are the same. Carefully check yourself against the rubric.

- [ ] Application still works correctly.
- [ ] `input_pokemon_type` extracted correctly.
    - Your main function should call this function where appropriate.
- [ ] `random_pokemon_type` extracted correctly.
    - Your main function should call this function where appropriate.

### Style Guide

- [ ] Appropriate and meaningful comments
- [ ] Code should be formatted neatly
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Must have type annotations
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.