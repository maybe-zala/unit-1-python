import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "PPNPNNDQDP\n", 
        '''Coins: 
Coin Summary:
Pennies (P): 4
Nickels (N): 3
Dimes (D): 2
Quarters (Q): 1
Total: $0.64'''
    ),
    (
        "QDNPPP\n", 
        '''Coins: 
Coin Summary:
Pennies (P): 3
Nickels (N): 1
Dimes (D): 1
Quarters (Q): 1
Total: $0.43'''
    ),
    (
        "DDGPPP\n",
        '''Coins: 
Warning: Unknown coin type 'G' ignored.
Coin Summary:
Pennies (P): 3
Nickels (N): 0
Dimes (D): 2
Quarters (Q): 0
Total: $0.23'''
    ),
    (
    "QDHLPP\n",
    '''Coins: 
Warning: Unknown coin type 'H' ignored.
Warning: Unknown coin type 'L' ignored.
Coin Summary:
Pennies (P): 2
Nickels (N): 0
Dimes (D): 1
Quarters (Q): 1
Total: $0.37'''
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
