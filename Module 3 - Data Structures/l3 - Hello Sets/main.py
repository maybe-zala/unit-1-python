# Ask the user to input plant heights separated by spaces
heights = input("Enter the height of the plants (space-separated): ")
set = {int(e) for e in heights.split(" ")}
mean : float = sum(set) / len(set)
print(f'Average height of distinct plants: {mean}')
    
#   Example input: 5 7 5 9 7

# Split the input string into individual elements (strings)

# Convert each height string into an integer

# Create a set from the list to eliminate duplicates

# Calculate the sum of the distinct heights

# Calculate the number of distinct heights

# Calculate the average

# Print the average height