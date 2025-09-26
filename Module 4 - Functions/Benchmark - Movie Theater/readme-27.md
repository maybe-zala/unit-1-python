# Functions - Benchmark: Movie Theater

In this benchmark, your job is to simulate purchasing a ticket at a movie theater. Your program should display all available movies, allow them to choose from those movies, then display all the available times for each movie and choose from there. Once the user chooses a movie, time, and quantity, their receipt should be displayed.

Movies:

- Demon Slayer The Movie
    - 4:05 PM, 7:10 PM
- Godzilla vs. Kong
    - 4:35 PM, 7:30 PM
- Raya and the Last Dragon
    - 3:50 PM, 7:05 PM

```
Welcome to the Movie Theater!
Each movie ticket costs $7.50.
Here are the currently showing movies and their times:
- Demon Slayer The Movie: 4:05 PM, 7:10 PM
- Godzilla vs. Kong: 4:35 PM, 7:30 PM
- Raya and the Last Dragon: 3:50 PM, 7:05 PM
What movie would you like to watch? Demon Slayer The Movie
Which showing time? 7:10 PM
How many tickets? 3
Thank you for your purchase! Enjoy your movie! Here is your receipt:

3 tickets for Demon Slayer The Movie @ 7:10 PM
Total: $22.5
```

## Functions to use:

- get_movie_choice(movies: Dict[str, List[str]]) -> str
Prompts the user to choose a movie from the list of available movies.
Displays the movie prompt.
Validates that the user's input matches a movie title from the list.
Keeps asking until a valid movie is entered.
Returns the selected movie title as a string.


- get_show_time(movie: str, show_times: List[str]) -> str
Asks the user to choose a showtime for the selected movie.
Displays only the times that are available for the selected movie.
Validates the input to make sure it's one of the listed times.
Keeps asking until a valid time is entered.
Returns the selected showtime as a string.


get_ticket_quantity() -> int
Asks the user how many tickets they want to buy.
Accepts numeric input only.
Ensures the number is greater than zero.
Keeps asking until a valid number is entered.
Returns the ticket quantity as an integer.


calculate_total(quantity: int) -> float

Calculates the total cost of the tickets.
Multiplies the ticket quantity by the fixed price ($7.50).
Returns the result as a float.

print_receipt(movie: str, time: str, quantity: int, total: float) -> None
Displays the final purchase receipt.
Formats and prints the receipt with:
Number of tickets
Movie title
Showtime
Total price (formatted to two decimal places)
Doesn't return anything (prints output directly).

### Rubric

- [ ] User can which movie they want to see
- [ ] User can which time they want to see the movie
    - They should only be able to choose times that are valid for the movie they chose
- [ ] User can choose how many tickets they want
- [ ] User is shown a receipt that displays their movie choice, time choice, ticket quantity choice, and total cost.

### Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.