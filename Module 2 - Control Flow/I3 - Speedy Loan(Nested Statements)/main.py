print('--- Speedy Loans ---')
print()
income= input('Income Level (High, Medium or Low): ')
if income == "High":
    print('Yes')
elif income== "Low":
    print("No")
else:
    credit=input('Credit Score(High or Low): ')

if credit == "Low":
    employment=input("Employment Type(Self or Salaried): ")
else:
    print("Yes")

if employment == "Self":
    print('No')
else:
    print("Yes")