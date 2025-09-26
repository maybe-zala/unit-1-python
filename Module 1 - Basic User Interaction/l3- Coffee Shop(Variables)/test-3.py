import subprocess
import platform
import difflib
import os

# Defined test cases
test_cases = [
    ("Brittany\nMagnolia Coffee\n1.00\n", '''Base Camp Coffee Shop Simulator 4000, Version 1.00
Copyright (C) 2024 BaseCamp Media, All Rights Reserved.

Let's collect some information before we start the game.

What is your name? What do you want to name your coffee shop? 
Thanks, Brittany. Let's set some initial pricing.

What do you want to charge per cup of coffee? 
Great. Here's what we've collected so far.

Your name is Brittany and you're opening Magnolia Coffee!
Your first cup of coffee will sell for $1.00.'''),
    ("Adam\nFresh Coffee\n3.00\n", '''Base Camp Coffee Shop Simulator 4000, Version 1.00
Copyright (C) 2024 BaseCamp Media, All Rights Reserved.

Let's collect some information before we start the game.

What is your name? What do you want to name your coffee shop? 
Thanks, Adam. Let's set some initial pricing.

What do you want to charge per cup of coffee? 
Great. Here's what we've collected so far.

Your name is Adam and you're opening Fresh Coffee!
Your first cup of coffee will sell for $3.00.''')
]

def normalize_newlines(text):
    return text.replace('\r\n', '\n').strip()

# Run test cases
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    print(f"Running Test Case {idx}:")
    
    os_name = platform.system()
    python_command = 'python3' if os_name == "Darwin" else 'python'

    try:
        process = subprocess.Popen(
            [python_command, 'coffee.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, errors = process.communicate(input=input_data)

        # Normalize newlines for comparison
        output = normalize_newlines(output)
        expected_output = normalize_newlines(expected_output)

        if output == expected_output:
            print("Test Passed!\n")
        else:
            print("Test Failed!")
            print("Difference:")
            diff = difflib.unified_diff(
                expected_output.splitlines(),
                output.splitlines(),
                lineterm=''
            )
            for line in diff:
                print(line)
            print()  # newline for readability

    except Exception as e:
        print(f"Error running test case {idx}: {e}")