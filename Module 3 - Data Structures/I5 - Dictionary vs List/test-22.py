import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "q", 
        '''Please provide the students names and then q to quit
> No students were provided'''
    ),
    ("britta\njeff\nabed\ntroy\nq\ncheck\nsign\nbritta\ncheck\nsign\nabed\ncheck\nq", 
        '''Please provide the students names and then q to quit
> > > > > [check] sign ins, [sign] in, or [q]uit:
> britta: N
jeff: N
abed: N
troy: N
[check] sign ins, [sign] in, or [q]uit:
> > [check] sign ins, [sign] in, or [q]uit:
> britta: Y
jeff: N
abed: N
troy: N
[check] sign ins, [sign] in, or [q]uit:
> > [check] sign ins, [sign] in, or [q]uit:
> britta: Y
jeff: N
abed: Y
troy: N
[check] sign ins, [sign] in, or [q]uit:
>'''),
    ("Brittany\nRjay\nSean\nq\ncheck\nsign\nSean\ncheck\nq",
    '''Please provide the students names and then q to quit
> > > > [check] sign ins, [sign] in, or [q]uit:
> Brittany: N
Rjay: N
Sean: N
[check] sign ins, [sign] in, or [q]uit:
> > [check] sign ins, [sign] in, or [q]uit:
> Brittany: N
Rjay: N
Sean: Y
[check] sign ins, [sign] in, or [q]uit:
>''' )
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