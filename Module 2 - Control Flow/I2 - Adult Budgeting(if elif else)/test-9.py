import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
   ("2300\n1100\n250\n300\n200", '''--- Budget Manager ---

Enter your monthly income: $Enter your monthly rent: $Enter your monthly utilities: $Enter your monthly groceries: $Enter other monthly expenses: $
Your budget is in good shape! You have $450.00 left for the month.'''),
("1950\n900\n200\n350\n500", '''--- Budget Manager ---

Enter your monthly income: $Enter your monthly rent: $Enter your monthly utilities: $Enter your monthly groceries: $Enter other monthly expenses: $
You are breaking even this month. Try to save some money or reduce expenses.'''),
("1200\n700\n150\n300\n100", '''--- Budget Manager ---

Enter your monthly income: $Enter your monthly rent: $Enter your monthly utilities: $Enter your monthly groceries: $Enter other monthly expenses: $
You're over budget by $50.00. Consider reducing some expenses or finding additional income sources.''')
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
        #print(f"Actual Output:\n{output}\n")
        diff = difflib.unified_diff(expected_output.splitlines(), output.splitlines(), lineterm='')
        print("Difference: ")
        print('\n'.join(diff))
