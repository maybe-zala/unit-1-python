# Legal Variables

We choose the names of our variables ourselves. But, there are some rules around creating a legal variable (a name we’re allowed to use).

Variable names may:
Use upper-case and lower-case letters
Use numbers
Use underscore characters (an underscore is the _ character)

If we name our variables like this, we won’t have any problems:

``` python

>>> my_variable = 6
>>> string6 = 7
>>> YourVariable = 88
```

There are also things we can’t do. When naming variables, we cannot:

* Use spaces
* Start with a number
* Use a [Reserved Word](https://docs.google.com/document/d/1NG3x8Q8T7RCPG1-9Di_BDPbtVckOdDgACbPXhAJqo20/edit?usp=sharing)
  
Look at what happens if we try to create an illegal variable:

``` python
# Using a space
>>> my variable = 6
  File "<stdin>", line 1
    my variable = 6
       ^^^^^^^^
SyntaxError: invalid syntax
```

``` python
# Starting with a number
>>> 2Variables = 6
  File "<stdin>", line 1
    2Variables = 6
    ^
SyntaxError: invalid decimal literal
```

``` python
# Using a reserved word
>>> del = 1
  File "<stdin>", line 1
    del = 1
        ^
SyntaxError: invalid syntax
```

## Examples

| Example    | Legal? | Notes                                                                                  |
|------------|--------|----------------------------------------------------------------------------------------|
| a          | yes    | Lower-case is fine                                                                     |
| time2go    | yes    | Numbers are fine                                                                       |
| 100ways    | no     | A variable cannot start with a number                                                   |
| A          | yes    | Upper-case is fine                                                                     |
| fun_times  | yes    | Underscores are allowed and recommended where there would normally be a space          |
| fun times  | no     | Spaces are not allowed                                                                 |
| FunTimes   | yes    | Capitalizing is fine                                                                   |
| _count     | yes    | Starting with an underscore is fine                                                     |
| fun!       | no     | Characters other than numbers, letters, and underscores are not allowed               |
