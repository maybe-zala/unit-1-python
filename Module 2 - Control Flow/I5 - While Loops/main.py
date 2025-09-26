coins= input("Coins: ").upper()
print()
pennies = 0
nickels = 0
dimes = 0
quarters = 0
counter = 0
while counter < len(coins):
    (coins[counter])
    if coins[counter] == 'P':
        pennies += 1
    elif coins[counter] == 'N':
        nickels += 1
    elif coins[counter] == 'D':
        dimes += 1
    elif coins[counter] == 'Q':
        quarters += 1
    else: 
        print(f"Warning: Unknown coin type '{coins[counter]}' ignored.")
    counter += 1

total = f"{(pennies*.01 + nickels*.05 + dimes*.10 + quarters*.25):.2f}"
print('Coin Summary:')
print('Pennies (P):',pennies)
print('Nickels (N):',nickels)
print('Dimes (D):',dimes)
print('Quarters (Q):',quarters)
print('Total: $'+total)