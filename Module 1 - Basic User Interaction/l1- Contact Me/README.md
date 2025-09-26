# Basic User Interaction - Intro 1: "Contact Me"

## Objectives

By the end of this assignment you should be able to:

- Use the print() function to display information to the user.
- Utilize the sep parameter in the print() function.
- Apply the end parameter in the print() function.
- Execute and evaluate test cases.
  
## Resources

- [Python print()](https://www.programiz.com/python-programming/methods/built-in/print)

## Assignment

Welcome to your first assignment! Your job is to display Sean's contact information.
You will display the information in the example.

- Sean's number should be displayed using the sep function.
- Sean's email should be displayed on two lines and should be connected at the @ using the end function.

### Example

```console
--------------------------------------------------
Name: Sean Ennis
Phone: 215-593-8075
Email: seanennis@basecampcodingacademy.org
--------------------------------------------------
```

## How to check your work

Now that you've got your code displaying information, it's time to run some test cases. When you execute the test file, you should see:

``` text
Running Test Case:
Test Passed!

```

If your code isn't quite right, you'll see:

``` text
Running Test Case:
Test Failed!
Expected Output:
--------------------------------------------------
Name: Sean Ennis
Phone: 215-593-8075
Email: seanennis@basecampcodingacademy.org
--------------------------------------------------

Actual Output:
** Here will be the actual output of your code. **
--------------------------------------------------
Name: Sean Adam
Phone: 215-593-8075
Email: seanennis@basecampcodingacademy.org
--------------------------------------------------

Differences:
** Here will be the differences between the actual output and expected output. **
--- 
+++ 
@@ -1,5 +1,5 @@
 --------------------------------------------------
-Name: Sean Ennis
+Name: Sean Adam
 Phone: 215-593-8075
 Email: seanennis@basecampcodingacademy.org
 --------------------------------------------------
```

### Common Misconceptions/Errors to Watch Out For

- print is not written with a capital P
- Missing parenthesis before/after the string
- Missing qoute at the beginning/end of text
- Pressing enter inside the string code creates a new line

### Rubric/Style Guide

- [ ] Display Sean full name.
- [ ] Display Sean's phone number seperated with a '-' using the sep function.
- [ ] Display Sean's email on two lines and connect them with the '@' using the end function.
- [ ] All test cases are passed.
