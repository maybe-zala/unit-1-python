def say_hello()-> str:
    return 'Hello World!'

def hey_you(name:str)-> str:
    return f"Hello {name}!"

def age_in_2050(birthyear:str)->int:
    return 2050-birthyear

def can_i_take_your_order(burgers:int,fries:int,drinks:int)->int:
    return burgers*4.50 + fries*1.50 + drinks*1.00