import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "1234\nenter\n1234\nchange\n1234\n4321\nenter\n4321\nenter\n1234\nchange\n4321\nhello\nenter\nhello\nquit", 
        '''What is the passcode? [enter], [change] passcode, [quit]> What is the passcode? You can enter.
[enter], [change] passcode, [quit]> What is the passcode? What should the new passcode be? [enter], [change] passcode, [quit]> What is the passcode? You can enter.
[enter], [change] passcode, [quit]> What is the passcode? Wrong passcode.
[enter], [change] passcode, [quit]> What is the passcode? What should the new passcode be? [enter], [change] passcode, [quit]> What is the passcode? You can enter.
[enter], [change] passcode, [quit]>'''
    ),
    (
        "5454\nenter\n5454\nchange\n343\nenter\n675\nenter\n5454\nquit", 
        '''What is the passcode? [enter], [change] passcode, [quit]> What is the passcode? You can enter.
[enter], [change] passcode, [quit]> What is the passcode? Wrong passcode.
[enter], [change] passcode, [quit]> What is the passcode? Wrong passcode.
[enter], [change] passcode, [quit]> What is the passcode? You can enter.
[enter], [change] passcode, [quit]>'''
    )
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