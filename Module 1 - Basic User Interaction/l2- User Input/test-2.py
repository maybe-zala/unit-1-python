import subprocess
import platform
import difflib

# Defined test cases
# For each set in the list:
    # The first index of the list should be the input and to be separated by "\n" for each input of the code.
    # The second index of the list should be what the output of the code should look like.
test_cases = [
   ("c\nc\nd\nb\na\n", '''Welcome to the Ms. Frizzle's Digital Quiz Quest!

Get ready to test your knowledge and have some fun.
Whether you're here to challenge yourself or just pass the time,
we've got a range of questions to keep you on your toes.

Good luck, and may the best brain win!

1. How do you display a message to the user in Python?
a) show()
b) echo()
c) print()
d) display()

Enter your answer: Correct Answer: c)

2. Which line of code prints Hello world! as one line of output?
a) print(Hello world!)
b) print("Hello", "world", "!")
c) print("Hello world!")
d) print("hello world")

Enter your answer: Correct Answer: c)

3. Which lines of code prints Hello world! as one line of output?
a) print("Hello")
   print(" world!")
b) print("Hello")
   print(" world!", end="")
c) print("Hello", sep="")
   print(" world!")
d) print("Hello", end="")
   print(" world!")

Enter your answer: Correct Answer: d)

4. What output is produced by the following statement?
print("555", "0123", sep="-")
a) 555 0123
b) 555-0123
c) 5550123-
d) 5-5-5-0-1-2-3

Enter your answer: Correct Answer: b)

5. In Python 3, which function is used to accept input from the user?
a) input()
b) raw_input()
c) rawinput()
d) string()

Enter your answer: Correct Answer: a)'''),
("a\nd\nc\nb\nc\n", '''Welcome to the Ms. Frizzle's Digital Quiz Quest!

Get ready to test your knowledge and have some fun.
Whether you're here to challenge yourself or just pass the time,
we've got a range of questions to keep you on your toes.

Good luck, and may the best brain win!

1. How do you display a message to the user in Python?
a) show()
b) echo()
c) print()
d) display()

Enter your answer: Correct Answer: c)

2. Which line of code prints Hello world! as one line of output?
a) print(Hello world!)
b) print("Hello", "world", "!")
c) print("Hello world!")
d) print("hello world")

Enter your answer: Correct Answer: c)

3. Which lines of code prints Hello world! as one line of output?
a) print("Hello")
   print(" world!")
b) print("Hello")
   print(" world!", end="")
c) print("Hello", sep="")
   print(" world!")
d) print("Hello", end="")
   print(" world!")

Enter your answer: Correct Answer: d)

4. What output is produced by the following statement?
print("555", "0123", sep="-")
a) 555 0123
b) 555-0123
c) 5550123-
d) 5-5-5-0-1-2-3

Enter your answer: Correct Answer: b)

5. In Python 3, which function is used to accept input from the user?
a) input()
b) raw_input()
c) rawinput()
d) string()

Enter your answer: Correct Answer: a)''')
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