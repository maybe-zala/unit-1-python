print("""How's My Grade Looking?

Class: Beating Guitar Hero 3

Assignments:

| Assignment            | Weight |
| --------------------- | ------ |
| Slow Ride             | 5%     |
| Barracuda             | 5%     |
| Bulls on Parade       | 10%    |
| Paint it Black        | 5%     |
| Even Flow             | 5%     |
| Holiday in Cambodia   | 5%     |
| Welcome to the Jungle | 10%    |
| The Metal             | 5%     |
| 3's & 7's             | 5%     |
| Cult of Personality   | 10%    |
| Cliffs of Dover       | 5%     |
| One                   | 5%     |
| Beat the game         | 25%    |
""")

grade_so_far = 0
points_available_so_far = 0

slow_ride_stars = int(input("How many stars did you get on Slow Ride [0-5]: "))
grade_so_far += slow_ride_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

barracuda_stars = int(input("How many stars did you get on Barracuda [0-5]: "))
grade_so_far += barracuda_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

bulls_on_parade_stars = int(input("How many stars did you get on Bulls On Parade [0-5]: "))
grade_so_far += bulls_on_parade_stars / 5 * 10
points_available_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

paint_it_black_stars = int(input("How many stars did you get on Paint it Black [0-5]: "))
grade_so_far += paint_it_black_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

even_flow_stars = int(input("How many stars did you get on Even Flow [0-5]: "))
grade_so_far += even_flow_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

holiday_in_cambodia_stars = int(input("How many stars did you get on Holiday In Cambodia [0-5]: "))
grade_so_far += holiday_in_cambodia_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

welcome_to_the_jungle_stars = int(input("How many stars did you get on Welcome to the Jungle [0-5]: "))
grade_so_far += welcome_to_the_jungle_stars / 5 * 10
points_available_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

the_metal_stars = int(input("How many stars did you get on The Metal [0-5]: "))
grade_so_far += the_metal_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

threes_and_sevens_stars = int(input("How many stars did you get on 3's & 7's [0-5]: "))
grade_so_far += threes_and_sevens_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

cult_of_personality_stars = int(input("How many stars did you get on Cult of Personality [0-5]: "))
grade_so_far += cult_of_personality_stars / 5 * 10
points_available_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

cliffs_of_dover_stars = int(input("How many stars did you get on Cliffs of Dover [0-5]: "))
grade_so_far += cliffs_of_dover_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

one_stars = int(input("How many stars did you get on One [0-5]: "))
grade_so_far += one_stars / 5 * 5
points_available_so_far += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")

did_beat_game = int(input("Did you beat the game [0 for no, 1 for yes]: "))
grade_so_far += did_beat_game * 25
points_available_so_far += 25
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_available_so_far + grade_so_far}")