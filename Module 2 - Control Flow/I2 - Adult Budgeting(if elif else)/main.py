print("--- Budget Manager ---")
print()
income=float(input('Enter your monthly income: $'))
rent=float(input('Enter your monthly rent: $'))
utilities=float(input('Enter your monthly utilities: $'))
groceries=float(input('Enter your monthly groceries: $'))
expenses=float(input('Enter other monthly expenses: $'))

expenses_total= (rent + utilities + groceries + expenses)
expenses_output = income - expenses_total

if expenses_output > 0:
    print(f"\nYour budget is in good shape! You have ${abs(expenses_output):.2f} left for the month.")
elif expenses_output == 0:
    print("\nYou are breaking even this month. Try to save some money or reduce expenses.")
else:
    print(f"\nYou're over budget by ${abs(expenses_output):.2f}. Consider reducing some expenses or finding additional income sources.")