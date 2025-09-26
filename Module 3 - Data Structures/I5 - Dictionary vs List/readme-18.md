# I5: Has Everyone Signed In Today


In this exercise you will build a small program for collecting student names and then allowing student to sign in and check if the whole class has arrived yet. Your application should start off collecting names from the user. Once they are finished providing names, you should allow the user to check whether or not each person has signed in, sign in a student, or quit.
> 
> 
> Example:
> 
> ```
> Please provide the students names and then q to quit
> > britta
> > jeff
> > abed
> > troy
> > q
> [check] sign ins, [sign] in, or [q]uit:
> > check
> britta: N
> jeff: N
> abed: N
> troy: N
> [check] sign ins, [sign] in, or [q]uit:
> > sign
> > britta
> [check] sign ins, [sign] in, or [q]uit:
> > check
> britta: Y
> jeff: N
> abed: N
> troy: N
> [check] sign ins, [sign] in, or [q]uit:
> > sign
> > abed
> [check] sign ins, [sign] in, or [q]uit:
> > check
> britta: Y
> jeff: N
> abed: Y
> troy: N
> [check] sign ins, [sign] in, or [q]uit:
> > q
> ```
> 
> Example:
> 
> ```
> Please provide the students names and then q to quit
> > q
> No students were provided
> ```

### Rubric
- [ ] must have comments
- [ ] User can provide an arbitrary amount of student names
- [ ] User can check in students
- [ ] User can view checkin status
- [ ] Program ends early and prints appropriate message if no students are provided
- [ ] Students and checkins are implemented using a single dictionary

### Style Guide
- [ ] Code should be formatted neatly
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
