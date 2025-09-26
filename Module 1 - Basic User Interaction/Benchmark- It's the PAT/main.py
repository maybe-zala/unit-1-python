print("Welcome, It's PAT your personal automated trainer!")
print()
user_weight=float(input('Enter your weight(lbs): '))
user_height=float(input('Enter your height in inches: '))
kg=float(0.45353)
meters=float(39.3701)
lbs_2_kg=(user_weight * kg)
inch_2_meters= user_height / meters
bmi= lbs_2_kg / inch_2_meters**2
print('\nResults:')
print(f'Weight in kilograms: {lbs_2_kg:.2f}')
print(f'Height in meters: {inch_2_meters:.2f}')
print(f'Your BMI is {bmi:.1f}')