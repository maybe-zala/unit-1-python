# Basic User Interaction - Intro 4: The Numerical Quest: Unraveling the Treasure Map 🗺️

## Objectives

By the end of this assignment you should be able to:

* Understand Basic Data Types
* Convert between different data types using casting functions (int(), float(), str(), etc.).
* Understand the difference between implicit and explicit type conversion.
* Perform basic mathematical operations

## Resources

### Related Videos

### Common Misconceptions/Errors to Watch Out For

* Use / for floating-point division and // for integer division.
* Be aware of floating-point precision issues; use the decimal module for higher precision when necessary.
* Explicitly convert between integers and floats using int() and float() as needed.
* Handle special numeric values (NaN, inf) and large numbers with care.
* Understand the type of variables and the results of operations involving different numeric types.

## Assignment

Background:
In a small town nestled between rolling hills, an old legend tells of a hidden treasure buried deep in the forest. The treasure map, however, is incomplete
and requires decoding. Local explorer Alex discovers the map but needs to solve a series of numeric puzzles to find the treasure's location.

The Numeric Puzzles:
The map is adorned with various numeric clues and mathematical challenges that Alex must solve to uncover the treasure’s exact coordinates. To assist in decoding
these clues, Alex ask you to build a custom-built Python program that performs various numeric operations.

### Initial Calculations

1. Alex begins by analyzing the first set of numeric clues on the map. The map provides two integers: Ask Alex for the two integers.
2. Alex needs to perform basic arithmetic operations on the two integers to unlock the next clue:

   * Sum: The map indicates that adding the numbers will reveal the next clue’s location.
   * Difference: Subtracting the numbers will help decode a hidden message.
   * Product: Multiplying the numbers shows the total distance to the treasure.
   * Quotient: Dividing the numbers provides the ratio for the next step in the quest.
   * Integer Division and Remainder: These results are used to adjust the coordinates on the map.

### Decoding Floating-Point Clues

3. The next part of the map features clues with two floating-point numbers: Ask Alex for the two floating-point numbers.
4. Alex needs to perform the following arithmetic operations on the two floating-point numbers to unlock the next clue:

   * Sum: Add the two floating point numbers.
   * Product: Then multipy these numbers to determine the exact position where the treasure is buried.

### Conversion Challenges

5. Some clues involve converting integers to floating-point numbers and vice versa. For instance, converting the first integer to a float and the first floating-point number 7.5 to an integer is required to unlock an encrypted section of the map.

### Calculatating coordinates

6. Finally, Alex needs to calculate coordinates based on the results you calculated:

   * Define two variables, x_coordinate and y_coordinate, to represent the x and y coordinates.
   * x_coordinate is calculated as the sum of sum_result (from integer addition) and float_sum (from floating-point addition).
   * y_coordinate is calculated as the difference between product_result (from integer multiplication) and quotient_result (from integer division).

### Uncovering the Treasure

After solving these numeric puzzles, Alex inputs the results into the map’s final coordinates. The Python program displays the results and helps Alex piece together the final location. The treasure chest is revealed beneath an ancient oak tree, filled with gold coins and relics from a bygone era.

## Example

```text
The Numerical Quest: Unraveling the Treasure Map

What is the first integer on the map? 15
What is the second integer on the map? 4

Integer Operations:
Sum: 15 + 4 = 19
Difference: 15 - 4 = 11
Product: 15 * 4 = 60
Quotient: 15 / 4 = 3.75
Integer Division: 15 // 4 = 3
Remainder: 15 % 4 = 3
Power: 15 ** 4 = 50625

What is the first floating point number on the map? 7.5
What is the second floating point number on the map? 2.5

Floating-Point Operations:
Sum: 7.5 + 2.5 = 10.0
Product: 7.5 * 2.5 = 18.75

Type Conversion:
Integer to Float: float(15) = 15.0
Float to Integer: int(7.5) = 7

Coordinates:
X Coordinate: 29.0
Y Coordinate: 56.25

The closest location to coordinates (29.0, 56.25) is: Burj Khalifa, Dubai
```

### Rubric/Style Guide

* [ ] All test cases are passed
* [ ] No sloppy/unnecessary/commented out code.
