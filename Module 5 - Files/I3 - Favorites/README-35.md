# Persistence - Intro 3: Favorites

In this exercise, you will write a program that helps a user remember their favorite things by reading and writing them to files.

You should ask the user whether they want to read a favorite, write a favorite, or quit the program. If they want to quit, of course you should quit. Otherwise, you should ask them what category of favorite they want to read or write.

```
[read], [write], [quit]> write
Favorite> fruit
Favorite fruit> pineapple
Wrote pineapple as favorite fruit.
> read
Favorite> book
You have not saved a favorite book.
[read], [write], [quit]> read
Favorite> fruit
Your favorite fruit is pineapple.
```

## Related Videos

- [Handling Missing Files](https://www.youtube.com/watch?v=94FIdWc9Pds&list=PL6xuclUa80Qi0WwO-fq10uoDDeg-UsLfd&index=4)
- [Paths](https://www.youtube.com/watch?v=H92v3Wx2Gik&list=PL6xuclUa80Qi0WwO-fq10uoDDeg-UsLfd&index=5)

## Related Textbook Sections

- Chapter 10 - Opening a File (page 173)
- Chapter 10 - Writing Files (page 182)

## Rubric

- [ ] Ask the user whether or not they want to read, write, or quit.
- [ ] Ask the user which "favorite."

## Style Guide

- [ ] Must include comments
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.
