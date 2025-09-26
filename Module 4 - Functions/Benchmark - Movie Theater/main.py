from typing import Dict, List

# Constants
TICKET_PRICE = 7.50

# Movie data
MOVIES = {
    "Demon Slayer The Movie": ["4:05 PM", "7:10 PM"],
    "Godzilla vs. Kong": ["4:35 PM", "7:30 PM"],
    "Raya and the Last Dragon": ["3:50 PM", "7:05 PM"]
}

# --- Helper Functions ---
def get_movie_choice(movie: Dict[str, List[str]]):
    while True:
        movies= input('What movie would you like to watch? ')
        if movies in movie:
            return movies
        else:
            print("Not a valid movie.")
def get_show_time(movie: str, show_times: List[str]):
    while True:
        show_time = input("Which showing time? ")
        if show_time in show_times:
            return show_time
        else:
            print('Please enter a valid time.')
            
def get_ticket_quantity():
   while True:
    tickets=input('How many tickets? ')
    if tickets.isdigit():
        if int(tickets)>0:
            return int(tickets)
    else:
        print("Invalid amount.")
def calculate_total(tickets: int):
    total = tickets * TICKET_PRICE
    return total
def print_receipt(movie: str, show_times: str, tickets: int, total: float):
    print('Thank you for your purchase! Enjoy your movie! Here is your receipt:')
    print(f'{tickets} tickets for {movie} @ {show_times}')
    print(f"${total}")





# --- Main Function ---

def main() -> None:
    print("Welcome to the Movie Theater!")
    print(f"Each movie ticket costs ${TICKET_PRICE:.2f}.")
    print("Here are the currently showing movies and their times:")
    for movie, times in MOVIES.items():
        print(f"- {movie}: {', '.join(times)}")

    movie_choice = get_movie_choice(MOVIES)
    time_choice = get_show_time(movie_choice, MOVIES[movie_choice])
    ticket_quantity = get_ticket_quantity()
    total_cost = calculate_total(ticket_quantity)

    print_receipt(movie_choice, time_choice, ticket_quantity, total_cost)

# --- Entry Point ---

if __name__ == '__main__':
    main()