print("Welcome to Good Burger.\nHome of the Good Burger.\nCan I take your order?")
print()


burgers = 0
fries = 0
drinks = 0
while True:
    burgers = input('Good Burgers ($4.50): ')
    if not burgers.isdigit():
        print('Quantity must be a positive number.')
    elif int(burgers) <= 0:
        print('Quantity must be a positive number.')
    else:
        burgers = int(burgers)
        break
while True:
    fries = input('French Fries ($1.50): ')
    if not fries.isdigit():
        print('Quantity must be a positive number.')
    elif int(fries) <= 0:
        print('Quantity must be a positive number.')
    else:
        fries = int(fries)
        break
while True:
    drinks = input('Drinks       ($1.00): ')
    if not drinks.isdigit():
        print('Quantity must be a positive number.')
    elif int(drinks) <= 0:
        print('Quantity must be a positive number.')
    else:
        drinks = int(drinks)
        break


burgers_sum=f"{(burgers * 4.50):.2f}"
fries_sum= f"{(fries * 1.50):.2f}"
drinks_sum= f"{(drinks * 1.00):.2f}"
total= f"{(float(burgers_sum) + float(fries_sum) + float(drinks_sum)):.2f}"
print()
print('Here is your reciept:')
print('- Good Burgers $4.50 x', burgers, ('= $')+ burgers_sum, sep=" ")
print('- French Fries $1.50 x', fries, ('= $')+ fries_sum, sep=" ")
print('- Drinks       $1.00 x', drinks, ('= $')+ drinks_sum, sep=" ")
print('TOTAL = $'+(total))
