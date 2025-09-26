import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "done\n", 
        '''[project] or [done]> No projects were provided.'''
    ),
    ("project\nProject 1\nNatalie\nI did a lot of science. I learned stuff good.\nproject\nEven More Science Than Other Science Things\nAbed\nLike... a lot more science.\ndone\nvote\nProject 1\nvote\nEven More Science Than Other Science Things\nvote\nProject 1\nvote\nProject 1\ndone", 
        '''[project] or [done]> Title: Student Name: Description: [project] or [done]> Title: Student Name: Description: [project] or [done]> [vote] or [done]> Which project (title)? [vote] or [done]> Which project (title)? [vote] or [done]> Which project (title)? [vote] or [done]> Which project (title)? [vote] or [done]> Project 1 is the winner!'''
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
