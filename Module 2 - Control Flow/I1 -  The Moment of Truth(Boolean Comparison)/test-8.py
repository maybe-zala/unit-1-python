import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
   ("5\n", '''***************************************
*                                     *
*   Welcome to the Moment of Truth!   *
*                                     *
***************************************

Get ready for an exciting challenge where your decisions matter!
Make the right choices, and you might just find out what truth lies ahead.

Good luck and enjoy the game!

Please enter a number: 
1. Is the number 5 less than 100?  True
2. Is the number 5 greater than 75?  False
3. Is the number 5 equal to 13?  False
4. Is the number 5 not equal to 18?  True
5. Is the number 5 less than or equal to 8?  True
6. Is the number 5 greater than or equal to 15?  False
7. Is the number 5 equal to 2 + 2?  False
8. Is the number 5 less than 2^5?  True
9. Is the number 5 equal to 30% of 20?  False
10. Is the number 5 divisible by 3  False
11. Is the number 5 less than 25?  True
12. Is the number 5 greater than 103?  False
13. Is the number 5 equal to 67?  False
14. Is the number 5 divisible by 5?  True
15. Is the number 5 less than or equal to 23?  True
16. Is the number 5 not equal to 15?  True
17. Is the number 5 equal to 7 * 5?  False
18. Is the number 5 less than 8?  True
19. Is the number 5 equal to 15% of 50?  False
20. Is the number 5 divisible by 8?  False
21. Is the number 5 divisible by 7?  False'''),
("9\n", '''***************************************
*                                     *
*   Welcome to the Moment of Truth!   *
*                                     *
***************************************

Get ready for an exciting challenge where your decisions matter!
Make the right choices, and you might just find out what truth lies ahead.

Good luck and enjoy the game!

Please enter a number: 
1. Is the number 9 less than 100?  True
2. Is the number 9 greater than 75?  False
3. Is the number 9 equal to 13?  False
4. Is the number 9 not equal to 18?  True
5. Is the number 9 less than or equal to 8?  False
6. Is the number 9 greater than or equal to 15?  False
7. Is the number 9 equal to 2 + 2?  False
8. Is the number 9 less than 2^5?  True
9. Is the number 9 equal to 30% of 20?  False
10. Is the number 9 divisible by 3  True
11. Is the number 9 less than 25?  True
12. Is the number 9 greater than 103?  False
13. Is the number 9 equal to 67?  False
14. Is the number 9 divisible by 5?  False
15. Is the number 9 less than or equal to 23?  True
16. Is the number 9 not equal to 15?  True
17. Is the number 9 equal to 7 * 5?  False
18. Is the number 9 less than 8?  False
19. Is the number 9 equal to 15% of 50?  False
20. Is the number 9 divisible by 8?  False
21. Is the number 9 divisible by 7?  False''')
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
