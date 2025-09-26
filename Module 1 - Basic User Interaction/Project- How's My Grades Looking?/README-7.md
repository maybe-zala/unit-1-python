# Basic User Interaction - How's My Grade Looking?

BCCA doesn't really use grades, but most courses do. Furthermore, many classes are passed or failed based on a combination of weighted grades. For example, consider the following grading policy from [Harvard's Introduction To Computer Science (CS50)](https://www.edx.org/course/cs50s-introduction-to-computer-science) taken from the [Fall 2019 Syllabus](https://cs50.harvard.edu/college/2019/fall/syllabus/).

![CS50 Expectations](cs50_expectations.png)
![CS50 Grading](cs50_weights.png)

Given these rules, we can know our best or worst possible grade after each assignment is graded. For example, if you never attend class you know that your best possible grade is a 90. Similarly, you know that you could get a 50 on the course's test and still get a 90 in the class.

Let's consider a simpler grading scheme and class schedule:

| Assignment | Weight |
|------------|--------|
| Homework 1 | 10%    |
| Homework 2 | 10%    |
| Quiz 1     | 10%    |
| Homework 3 | 10%    |
| Test 1     | 20%    |
| Homework 4 | 10%    |
| Quiz 2     | 10%    |
| Test 2     | 20%    |

Your task for this assignment is to create a program that allows a student to provide their grades for each assignment in a course of your own design and print out the best and worst possible grade they could possibly achieve for the course.

Here is some hypothetical output given the schedule above:

## Example

```console
Homework 1: 80
Best Possible = 98.0
Worst Possible = 8.0
Homework 2: 100
Best Possible = 98.0
Worst Possible = 18.0
Quiz 1: 50
Best Possible = 93.0
Worst Possible = 23.0
...
```

Finally, have some fun! Come up with a course and assignment names. Teach a course on Programming, Memeology, Organic Chemistry, or TikTok for Senior Citizens. It's up to you!

I've provided an example solution for you in `example_solution.py`. To run the example solution, open up the "Shell" on the right of this web page and enter `python example_solution.py` into the shell.

### Rubric/Style Guide

- [ ] Custom course and assignments
- [ ] At least 6 different assignments graded
- [ ] At least 3 different weights
- [ ] Best and worst possible grade shown after each grade input
- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.