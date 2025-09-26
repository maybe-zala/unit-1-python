import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
    ("2\n3\n4\n", "Welcome to Good Burger.\nHome of the Good Burger.\nCan I take your order?\n\nGood Burgers ($4.50): French Fries ($1.50): Drinks       ($1.00): \nHere is your receipt:\n- Good Burgers $4.50 x 2 = $9.00\n- French Fries $1.50 x 3 = $4.50\n- Drinks       $1.00 x 4 = $4.00\nTOTAL = $17.50"),
    ("1\n2\n3\n", "Welcome to Good Burger.\nHome of the Good Burger.\nCan I take your order?\n\nGood Burgers ($4.50): French Fries ($1.50): Drinks       ($1.00): \nHere is your receipt:\n- Good Burgers $4.50 x 1 = $4.50\n- French Fries $1.50 x 2 = $3.00\n- Drinks       $1.00 x 3 = $3.00\nTOTAL = $10.50")
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
        print(f"Expected Output:\n{expected_output}\n")
        print(f"Actual Output:\n{output}\n")
        diff = difflib.unified_diff(expected_output.splitlines(), output.splitlines(), lineterm='')
        print("Difference: ")
        print('\n'.join(diff))