# Project 2: Bomber's Hideout Code

![Bomber's Secret Society of Justice](Bombers_Secret_Society_of_Justice.png)

In [The Legend of Zelda: Majora's Mask](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Majora%27s_Mask) there is a gang of small boys called the [Bomber's Secret Society of Justice](https://zelda.fandom.com/wiki/Bombers_Secret_Society_of_Justice). They spend their time running around Clocktown trying to help out villagers and make them happy. Like every good secret society, they have a secret hideout. To protect this hideout, they only let some in if they have the passcode. On top of that, they regularly change the passcode!

In this program you will write a program that keeps up with the passcode to get into the hideout. Users can try to enter the hideout, change the passcode, or quit the program. Entering the hideout and changing the passcode both require the current passcode. If the user provides the wrong password, you should tell that it is wrong.

**Example:**

```
What is the passcode? 1234
[enter], [change] passcode, [quit]> enter
What is the passcode? 1234
You can enter.
[enter], [change] passcode, [quit]> change
What is the passcode? 1234
What should the new passcode be? 4321
[enter], [change] passcode, [quit]> enter
What is the passcode? 4321
You can enter.
[enter], [change] passcode, [quit]> enter
What is the passcode? 1234
Wrong passcode.
[enter], [change] passcode, [quit]> change
What is the passcode? 4321
What should the new passcode be? hello
[enter], [change] passcode, [quit]> enter
What is the passcode? hello
You can enter.
[enter], [change] passcode, [quit]> quit
```

## Rubric

- [ ] Ask for the passcode at the beginning.
- [ ] Allow the user to enter the hideout if they provide the correct passcode
- [ ] Disallow the user from entering the hideout if they provide the wrong passcode
- [ ] Allow the user to change the passcode if they provide the correct passcode
- [ ] Disallow the user from changing the passcode if they provide the wrong passcode
- [ ] Display an error message if the user chooses an invalid action.
- [ ] Allow the user to quit the program
- [ ] Use a single `while` loop

### Style Guide
- [ ] Appropriate and meaniful comments
- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.