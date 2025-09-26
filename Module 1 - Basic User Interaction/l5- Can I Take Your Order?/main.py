fprint("Welcome to Good Burger.\nHome of the Good Burger.\nCan I take your order?")
print()
burgers = int(input('Good Burgers ($4.50): '))
fries= int(input('French Fries ($1.50): '))
drinks= int(input('Drinks       ($1.00): '))
burgers_sum= f"{(burgers * 4.50):.2f}"
fries_sum= f"{(fries * 1.50):.2f}"
drinks_sum= f"{(drinks * 1.00):.2f}"
total= f"{(float(burgers_sum) + float(fries_sum) + float(drinks_sum)):.2f}"
print('\nHere is your receipt:')
print('- Good Burgers $4.50 x', burgers, ('= $')+ burgers_sum, sep=" ")
print('- French Fries $1.50 x', fries, ('= $')+ fries_sum, sep=" ")
print('- Drinks       $1.00 x', drinks, ('= $')+ drinks_sum, sep=" ")
print('TOTAL = $'+(total))
