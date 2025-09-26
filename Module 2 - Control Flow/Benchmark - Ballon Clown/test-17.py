import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "dog\npump\npump\npump", 
        '''I can make a sword, dog, or the triforce.
Which balloon do you want? Balloon: dog
Capacity: 7
Current: 0
[pump] air, [release] air, [tie] balloon> Balloon: dog
Capacity: 7
Current: 3
[pump] air, [release] air, [tie] balloon> Balloon: dog
Capacity: 7
Current: 6
[pump] air, [release] air, [tie] balloon> POP!'''
    ),
    ("triforce\npump\nrelease\nrelease\npump\npump\npump\nrelease\npump\ntie", 
        '''I can make a sword, dog, or the triforce.
Which balloon do you want? Balloon: triforce
Capacity: 11
Current: 0
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 3
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 1
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 0
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 3
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 6
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 9
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 7
[pump] air, [release] air, [tie] balloon> Balloon: triforce
Capacity: 11
Current: 10
[pump] air, [release] air, [tie] balloon> Here is your triforce balloon!'''
    ),
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
