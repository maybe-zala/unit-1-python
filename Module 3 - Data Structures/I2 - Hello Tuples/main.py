# Tuple containing the module names
modules = (
    "Basic User Interaction",
    "Control Flow",
    "Data Structures",
    "Functions",
    "File Handling",
    "Dataclasses",
    "OOP",
    "SQL",
    "Testing",
    "Libraries"
)

module_number = input("Which module? ")
if not module_number .isdigit():
        print('Invalid input. Please enter a numeric value.')
        quit()


if int(module_number) >= 11 or int(module_number) < 1:
    print('Invalid module number. Please enter a number between 1 and 10.')
    quit()
print(f"Module {module_number} : {modules[int(module_number) - 1]}")