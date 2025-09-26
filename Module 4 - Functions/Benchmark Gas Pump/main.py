

def before_or_after():
    print("Pay before or after?")
    
def get_grade():
    print('What grade?')
    print('- Regular $2.50/gal\n- Mid-grade $3.00/gal\n- Premium $3.50/gal')
def get_gallons():
    print('How many gallons did you pump?')
    gallons=input('> ')
def calculate_total_cost():
    print(f'Gallons purchased: {amount/grade_price}')
   
   
before_or_after()
pay=input('> ')
if pay == "before":
        print("How much are you spending?")
        amount=input('> ')
        get_grade()
        grade=input('> ')
        if grade.lower == "regular":
            grade_price=2.50
        if grade.lower == "mid-grade":
            grade_price=3.00
        if grade.lower == "premium":
            grade_price=3.50
            print('Thank you for your purchase!')
            print(f'Payment: {pay}')
            print(f'Amount spent: {amount}')
            print(f'Gallons purchased: {get_gallons}')
            calculate_total_cost()
if pay == "after":
        get_grade()
        grade=input('> ')
        if grade.lower == "regular":
            grade_price=2.50
        if grade.lower == "mid-grade":
            grade_price=3.00
        if grade.lower == "premium":
            grade_price=3.50
        get_gallons()
        gallons=input('> ')
        print('Thank you for your purchase!')
        print(f'Payment: {pay}')
        print(f'Amount spent: {calculate_total_cost()}')
        print(f'Gallons purchased: {gallons}')
