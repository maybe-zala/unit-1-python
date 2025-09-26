# Functions - Benchmark: Gas Pump

In this benchmark, your task is to simulate a self-service, point-of-sale system for a gas pump. Your gas pump should allow the user to specify whether they want to prepay or pay after pumping. It should also allow them to choose between regular, mid-grade, and premium gas. Please refer to the rubric, example below, and test cases for more specific details.

Examples:

```
Pay before or after?
> before
How much are you spending?
> 10
What grade?
- Regular $2.50/gal
- Mid-grade $3.00/gal
- Premium $3.50/gal
> Regular
Thank you for your purchase!
Payment: before
Amount spent: $10.00
Gallons purchased: 4.0
```

```
Pay before or after?
> after
What grade?
- Regular $2.50/gal
- Mid-grade $3.00/gal
- Premium $3.50/gal
> Mid-grade
How many gallons of gas did you pump?
> 5
Thank you for your purchase!
Payment: after
Amount spent: $15.00
Gallons purchased: 5.0
```

### Rubric

- [ ] create four functions
    - before_or_after
        - takes in 1 argument
    - get_grade
        - takes in 1 argument
    - get_gallons 
        - takes in 2 argument
    - calculate_total_cost
        - takes in 2 arguments

- [ ] User can choose to prepay or pay after
    - If the user chooses to prepay, they provide the amount of money that they are spending and you calculate the appropriate amount of gas.
    - If the user chooses pay after, they provide the amount of gas that they are purchasing and you calculate the total cost.
- [ ] User can choose choose gas type
    - Options: Regular ($2.50/gal), Mid-Grade ($3.00/gal), Premium ($3.50/gal)
- [ ] Must use write (and use) at least 1 function in addition to `main`

### Style Guide

- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file.
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.