import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
   ("15\n4\n7.5\n2.5\n", '''The Numerical Quest: Unraveling the Treasure Map

What is the first integer on the map? What is the second integer on the map? 
Integer Operations:
Sum: 15 + 4 = 19
Difference: 15 - 4 = 11
Product: 15 * 4 = 60
Quotient: 15 / 4 = 3.75
Integer Division: 15 // 4 = 3
Remainder: 15 % 4 = 3
Power: 15 ** 4 = 50625

What is the first floating point number on the map? What is the second floating point number on the map? 
Floating-Point Operations:
Sum: 7.5 + 2.5 = 10.0
Product: 7.5 * 2.5 = 18.75

Type Conversion:
Integer to Float: float(15) = 15.0
Float to Integer: int(7.5) = 7

Coordinates:
X Coordinate: 29.0
Y Coordinate: 56.25

The closest location to coordinates (29.0, 56.25) is: Burj Khalifa, Dubai'''),
("2\n5\n5.5\n1.5\n", '''The Numerical Quest: Unraveling the Treasure Map

What is the first integer on the map? What is the second integer on the map? 
Integer Operations:
Sum: 2 + 5 = 7
Difference: 2 - 5 = -3
Product: 2 * 5 = 10
Quotient: 2 / 5 = 0.4
Integer Division: 2 // 5 = 0
Remainder: 2 % 5 = 2
Power: 2 ** 5 = 32

What is the first floating point number on the map? What is the second floating point number on the map? 
Floating-Point Operations:
Sum: 5.5 + 1.5 = 7.0
Product: 5.5 * 1.5 = 8.25

Type Conversion:
Integer to Float: float(2) = 2.0
Float to Integer: int(5.5) = 5

Coordinates:
X Coordinate: 14.0
Y Coordinate: 9.6

The closest location to coordinates (14.0, 9.6) is: Eiffel Tower, Paris''')
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