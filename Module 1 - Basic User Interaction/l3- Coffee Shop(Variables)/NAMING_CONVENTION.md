# Python's Variable Naming Conventions

We know there are rules around which variable names are legal. But there are still some ‘rules’
around how to choose good variable names. This is called a Naming Convention. **Just because a
variable name is legal doesn't mean it's a good choice.** Python naming convention is often referred
to as snake case. Snake case is a way of writing phrases without spaces, where spaces are replaced with
underscores _ , and the words are typically all lower case.

Here are the ‘rules’:

* Variables should always start with a lower-case character
* Use underscores instead of spaces to separate words
* Don’t use upper-case characters
* Starting with underscores is ok, but is used for a special purpose

## Example

| Example       | Conventional? | Notes                                                            |
|---------------|---------------|------------------------------------------------------------------|
| my_variable   | yes           | Use underscores for spaces between words                        |
| Myvariable    | no            | Variables shouldn’t start with an upper-case letter              |
| myVariable    | no            | Variables shouldn’t use upper-case characters                    |
| _my_variable  | possibly      | Starting with an underscore is ok, but it’s used for a special purpose |

## Do Variable Naming Conventions Matter?

Does it even matter if we follow convention? Not to Python! Python will not make us follow convention at all. It only cares if variable names are legal.
**It’s not important to Python, but it is important to us, the programmer. It’s especially helpful for other programmers when they read our code.**
Other programming languages also have naming conventions. Each language has its own rules to follow
For example, JavaScript has a convention called camelCase
