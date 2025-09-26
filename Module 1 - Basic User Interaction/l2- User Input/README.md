# Basic User Interaction - Intro 2: Ms. Frizzle's Digital Quiz Quest

## Objectives

By the end of this assignment you should be able to:

- understand the importance of user interaction in programming and its role in creating interactive applications.
- understand how user input and output facilitate communication between the user and the program.
- use the input() function to collect user input.

## Resources

![User Input](https://www.youtube.com/watch?v=hcNB9twfM0s)

## Assignment

Now that we’ve learned how to display text, let’s explore how to capture user responses and build an interactive program
Ms. Valerie Frizzle, an innovative and enthusiastic teacher at Innovative Horizons Academy, is gearing up for the new school year. Known for her creative and interactive teaching methods, Ms. Frizzle is determined to bring her quizzes into the digital age. Her goal is to transition from the traditional pen-and-paper format to an interactive digital quiz that will engage her students.

To achieve this, Ms. Frizzle has enlisted your help. Armed with your newly acquired programming skills, you are tasked with creating a dynamic and interactive quiz that will captivate her students and make learning more exciting.

### Example

```console
Welcome to the Ms. Frizzle's Digital Quiz Quest! 🚌✨ 

Get ready to test your knowledge and have some fun.
Whether you're here to challenge yourself or just pass the time,
we've got a range of questions to keep you on your toes.

Good luck, and may the best brain win! 🚀

1. How do you display a message to the user in Python?
a) show()
b) echo()
c) print()
d) display()

Enter your answer: c
Correct Answer: c)

2. Which line of code prints Hello world! as one line of output?
a) print(Hello world!)
b) print("Hello", "world", "!")
c) print("Hello world!")
d) print("hello world")      

Enter your answer: c
Correct Answer: c)

3. Which lines of code prints Hello world! as one line of output?
a) print("Hello")
   print(" world!")
b) print("Hello")
   print(" world!", end="")
c) print("Hello", sep="")
   print(" world!")   
d) print("Hello", end="")
   print(" world!")       

Enter your answer: d
Correct Answer: d)

4. What output is produced by the following statement?
print("555", "0123", sep="-")
a) 555 0123
b) 555-0123 
c) 5550123-
d) 5-5-5-0-1-2-3  

Enter your answer: b
Correct Answer: b)

5. In Python 3, which function is used to accept input from the user    
a) input()
b) raw_input()
c) rawinput()
d) string()

Enter your answer: a
Correct Answer: a)

```

### Common Misconceptions/Errors to Watch Out For

- The input() function always returns the user’s input as a string. If you need a different type, such as an integer or float, you must explicitly convert it.
- Numeric inputs are handled like strings.
- input() is a blocking call, meaning it will wait until the user provides input before proceeding. This can affect the flow of the program, especially in more complex applications.
- Pressing enter inside the string code creates a new line

### Rubric/Style Guide

- [ ] Display the welcome message
- [ ] Display all quiz questions and answer choices
- [ ] Allows user to input an answer to the question
- [ ] All test cases are passed

