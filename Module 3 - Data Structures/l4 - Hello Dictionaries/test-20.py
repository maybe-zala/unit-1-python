import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [ 
    (
        "books\nauthor\nHarry Potter\nquit", 
        '''view [books], show [author], [quit]> Harry Potter
Effective Testing with RSpec 3
Automate the Boring Stuff
Quiet
Peak
view [books], show [author], [quit]> book> JK Rowling
view [books], show [author], [quit]>'''
    ),
    (
        "author\nQuiet\nauthor\nPeak\nquit", 
        '''view [books], show [author], [quit]> book> Susan Cain
view [books], show [author], [quit]> book> Anders Ericsson
view [books], show [author], [quit]>''')
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