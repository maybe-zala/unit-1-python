import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "Add\nVideo Games\nAdd\nHomework\nView\nRemove\nVideo Gam\nRemove\nHomework\nView\nquit\nq", 
        '''Welcome to Count your Blessings!

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Enter something you are thankful for: 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Enter something you are thankful for: 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
You are thankful for the following 2 item(s):
1. Video Games
2. Homework

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Which item would you like to delete? This item is not in your Thankful Box!

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Which item would you like to delete? 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
You are thankful for the following 1 item(s):
1. Video Games

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: invalid input

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit:'''
    ),
    (
        "Add\nFamily\nAdd\nFriends\nAdd\nMoney\nUpdate\nMoney\nMy pet\nAdd\nMy house\nRemove\nhouse\nView\nRemove\nMy house\nView\nq", 
        '''Welcome to Count your Blessings!

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Enter something you are thankful for: 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Enter something you are thankful for: 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Enter something you are thankful for: 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Which item would you like to update? What would you like to change it to? 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Enter something you are thankful for: 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Which item would you like to delete? This item is not in your Thankful Box!

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
You are thankful for the following 4 item(s):
1. Family
2. Friends
3. My pet
4. My house

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
Which item would you like to delete? 
[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit: 
You are thankful for the following 3 item(s):
1. Family
2. Friends
3. My pet

[Add] blessing, [Remove] blessing, [Update] blessing, [View] blessings or [q] to quit:'''
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
