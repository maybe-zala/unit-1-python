import math
import location

# Display welcome message
print("The Numerical Quest: Unraveling the Treasure Map")
print()
# Ask for the integers on the map
integer1=int(input("What is the first integer on the map? "))
integer2=int(input("What is the second integer on the map? "))
# Basic arithmetic operations
print('\nInteger Operations:')
sum1=integer1+integer2
difference= integer1 - integer2
product=integer1 * integer2
quotient=integer1/integer2
integer_division= integer1 //integer2
remainder= integer1 %  integer2
power= integer1 ** integer2
# Display results
print(f"Sum: {integer1} + {integer2} = {sum1}")
print(f"Difference: {integer1} - {integer2} = {difference}")
print(f"Product: {integer1} * {integer2} = {product}")
print(f'Quotient: {integer1} / {integer2} = {quotient}')
print(f'Integer Division: {integer1} // {integer2} = {integer_division}')
print(f'Remainder: {integer1} % {integer2} = {remainder}')
print(f'Power: {integer1} ** {integer2} = {power}')
print()
# Ask for the floating point numbers on the map
float1=float(input('What is the first floating point number on the map? '))
float2=float(input('What is the second floating point number on the map? '))
# Floating-point arithmetic
print('\nFloating-Point Operations:')
sum2=float1+float2
product2=float1*float2
print(f"Sum: {float1} + {float2} = {sum2}")
print(f"Product: {float1} * {float2} = {product2}")
# Type conversion
float=float(integer1)
int=int(float1)
# Display results
print("\nType Conversion:")
print(f"Integer to Float: float({integer1}) =", float)
print(f"Float to Integer: int({float1}) =", int)
print()
#Calculate coordinates
print('Coordinates:')
x_coordinate=sum1+sum2
print('X Coordinate:',x_coordinate)
y_coordinate=product-quotient
print("Y Coordinate:",y_coordinate)
 #Displays location(Do not edit)
closest_location = location.find_closest_location(x_coordinate, y_coordinate)
print(f"\nThe closest location to coordinates ({x_coordinate}, {y_coordinate}) is: {closest_location}")