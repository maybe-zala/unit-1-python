import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "book\nHow to Design Programs\nFelleisen et al\nbook\nStructure and Intepretation of Computer Programs\nAbelson and Sussman\nview\nloan\n2\nBrittany\nview\nloan\n1\nEthan\nreturn\nStructure and Intepretation of Computer Programs\nBrittany\nview\nquit", 
        '''add [book], [view] inventory, [loan] book, [return] book, [quit]?
> Title?
> Author(s)?
> add [book], [view] inventory, [loan] book, [return] book, [quit]?
> Title?
> Author(s)?
> add [book], [view] inventory, [loan] book, [return] book, [quit]?
> 1. [Available] How to Design Programs by Felleisen et al
2. [Available] Structure and Intepretation of Computer Programs by Abelson and Sussman
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> Which book?
1. How to Design Programs by Felleisen et al
2. Structure and Intepretation of Computer Programs by Abelson and Sussman
> Borrower's name?
> add [book], [view] inventory, [loan] book, [return] book, [quit]?
> 1. [Available] How to Design Programs by Felleisen et al
2. [Unavailable] Structure and Intepretation of Computer Programs by Abelson and Sussman
add [book], [view] inventory, [loan] book, [return] book, [quit]?
> Which book?
1. How to Design Programs by Felleisen et al
> Borrower's name?
> add [book], [view] inventory, [loan] book, [return] book, [quit]?
> Title?
> Borrower's Name?
> add [book], [view] inventory, [loan] book, [return] book, [quit]?
> 1. [Unavailable] How to Design Programs by Felleisen et al
2. [Available] Structure and Intepretation of Computer Programs by Abelson and Sussman
add [book], [view] inventory, [loan] book, [return] book, [quit]?
>''' )
]

# Run test cases
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    print(f"Running Test Case {idx}:")
    
    os_name = platform.system()
    python_command = 'python3' if os_name == 'Darwin' else 'python'
    
    # Run the main.py file
    process = subprocess.Popen(
        [python_command, 'main.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, _ = process.communicate(input=input_data)
    output = output.strip()

    if output == expected_output:
        print("Test Passed!\n")
    else:
        print("Test Failed!")
        diff = difflib.unified_diff(
            expected_output.splitlines(),
            output.splitlines(),
            lineterm=''
        )
        print("🔍 Difference:")
        print('\n'.join(diff))