import subprocess
import platform
import difflib

# Defined test cases
test_case = '''--------------------------------------------------
Name: Sean Ennis
Phone: 215-593-8075
Email: seanennis@basecampcodingacademy.org
--------------------------------------------------'''

# Run test cases
print(f"Running Test Case:")
# This returns the operating system name as a string, such as 'Windows', 'Linux', or 'Darwin' (for macOS).
os_name = platform.system()

# This is choosing the python version (based on operating system) and file name.
if os_name == "Darwin":
    process = subprocess.Popen(['python3', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
else:
    process = subprocess.Popen(['python', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, _ = process.communicate()
output = output.strip()

if output == test_case:
    print("Test Passed!\n")
else:
    print("Test Failed!")
    #print(f"Expected Output:\n{test_case}\n")
    #print(f"Actual Output:\n{output}\n")
    expected_output = test_case
    diff = difflib.unified_diff(expected_output.splitlines(), output.splitlines(), lineterm='')
    print("Difference: ")
    print('\n'.join(diff))