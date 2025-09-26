num = int(input("Enter a number between 1 - 10: "))
day = num * 3 #changed to multiplication
year = (round(12.65 ** 3))
first_name = input("Enter a name: ")
#changed firstname to first_name
adjective = input("Enter an adjective: ")
#lowercased adjective
type_of_bird= input("Enter a type of bird: ")
#added type_of_bird variable and input
verb_past_tense = "ran"
#changed run to past tense, ran
num_of_stairs = 57-23
#57-23=34
amount_1 = 0.33
#changed to amount_1
amount_2 = 24.25
#changed to amount_2
ounces = f"{(amount_1 * amount_2):.1f}"
#multiplied amount 1 and 2 and rounded to hundredths place

monthly_price = float(input("Enter a price: $"))
yearly_price = float(round((monthly_price * 12) - 10, 2))
monthly_price = f"{monthly_price:.2f}"
yearly_price = f"{yearly_price:.2f}"







#Do not touch code below
print(f'''
It was November {day}, {year}, {first_name} woke up to the {adjective} smell of {type_of_bird} roasting in the kitchen downstairs. They {verb_past_tense} down 
the {num_of_stairs} stairs to see if they could help with dinner. Their mom said, 'See if your father needs a fresh drink.' So they carried a tray of {ounces} oz 
glasses full of lemonade into the living room. When they got there, they couldn't believe their eyes! To finish this story please subscribe for the low 
monthly price of ${monthly_price} or for even more savings our yearly price of ${yearly_price}.
''')

