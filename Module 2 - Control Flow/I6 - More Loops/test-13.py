import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "1\n1\n1\n", 
        '''Welcome to Good Burger.
Home of the Good Burger.
Can I take your order?

Good Burgers ($4.50): French Fries ($1.50): Drinks       ($1.00): 
Here is your reciept:
- Good Burgers $4.50 x 1 = $4.50
- French Fries $1.50 x 1 = $1.50
- Drinks       $1.00 x 1 = $1.00
TOTAL = $7.00'''
    ),
    (
        "-2\n2\n3\napples\n4\n", 
        '''Welcome to Good Burger.
Home of the Good Burger.
Can I take your order?

Good Burgers ($4.50): Quantity must be a positive number.
Good Burgers ($4.50): French Fries ($1.50): Drinks       ($1.00): Quantity must be a positive number.
Drinks       ($1.00): 
Here is your reciept:
- Good Burgers $4.50 x 2 = $9.00
- French Fries $1.50 x 3 = $4.50
- Drinks       $1.00 x 4 = $4.00
TOTAL = $17.50'''
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
