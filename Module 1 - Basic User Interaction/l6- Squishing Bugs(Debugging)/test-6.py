import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
    ("5\nAmber\npretty\nsparrow\n1.50\n", '''Enter a number between 1 - 10: Enter a name: Enter an adjective: Enter a type of bird: Enter a price: $
It was November 15, 2024, Amber woke up to the pretty smell of sparrow roasting in the kitchen downstairs. They ran down 
the 34 stairs to see if they could help with dinner. Their mom said, 'See if your father needs a fresh drink.' So they carried a tray of 8.0 oz 
glasses full of lemonade into the living room. When they got there, they couldn't believe their eyes! To finish this story please subscribe for the low 
monthly price of $1.50 or for even more savings our yearly price of $8.00.'''),
    ("2\nSam\nstrong\nturkey\n2.35\n", '''Enter a number between 1 - 10: Enter a name: Enter an adjective: Enter a type of bird: Enter a price: $
It was November 6, 2024, Sam woke up to the strong smell of turkey roasting in the kitchen downstairs. They ran down 
the 34 stairs to see if they could help with dinner. Their mom said, 'See if your father needs a fresh drink.' So they carried a tray of 8.0 oz 
glasses full of lemonade into the living room. When they got there, they couldn't believe their eyes! To finish this story please subscribe for the low 
monthly price of $2.35 or for even more savings our yearly price of $18.20.''')
]

# Run test cases
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    print(f"Running Test Case {idx}:")
    # This returns the operating system name as a string, such as 'Windows', 'Linux', or 'Darwin' (for macOS).
    os_name = platform.system()

    # This is choosing the python version (based on operating system) and file name.
    if os_name == "Darwin":
        process = subprocess.Popen(['python3', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    else:
        process = subprocess.Popen(['python', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate(input=input_data)
    output = output.strip()
    
    if output == expected_output:
        print("Test Passed!\n")
    else:
        print("Test Failed!")
        #print(f"Expected Output:\n{expected_output}\n")
        print(f"Actual Output:\n{output}\n")
        diff = difflib.unified_diff(expected_output.splitlines(), output.splitlines(), lineterm='')
        print("Difference: ")
        print('\n'.join(diff))