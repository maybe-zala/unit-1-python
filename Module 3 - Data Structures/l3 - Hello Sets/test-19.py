import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "5 9 10 17 19\n", 
        '''Enter the height of the plants (space-separated): Average height of distinct plants: 12.0'''
    ),
    (
        "1 2 3 4 5\n", 
        '''Enter the height of the plants (space-separated): Average height of distinct plants: 3.0'''
    ),
    (
        "33 60 24 70 33\n",
        '''Enter the height of the plants (space-separated): Average height of distinct plants: 46.75'''
    ),
      (
        "33 60 24 70 33\n",
        '''Enter the height of the plants (space-separated): Average height of distinct plants: 46.75'''
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