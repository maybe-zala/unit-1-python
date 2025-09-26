import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
   ("120\n65\n", '''Welcome, It's PAT your personal automated trainer!

Enter your weight(lbs): Enter your height in inches: 
Results:
Weight in kilograms: 54.42
Height in meters: 1.65
Your BMI is 20.0'''),
("205\n60\n", '''Welcome, It's PAT your personal automated trainer!

Enter your weight(lbs): Enter your height in inches: 
Results:
Weight in kilograms: 92.97
Height in meters: 1.52
Your BMI is 40.0''')
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