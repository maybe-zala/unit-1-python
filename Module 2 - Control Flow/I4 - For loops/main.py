vowels: int = 0

user_input=input("Enter a string: ")

for x in user_input:   
    user_input = x.lower()
    if user_input== 'a' or user_input=='e'or user_input=='i'or user_input=='o'or user_input=='u':
        vowels+=1
print(f"Number of vowels: {vowels}")
rows= int(input("Enter the number of rows for the diamond:"))
for x in range(1, rows+1):
    row_space = ' ' * (rows - x)
    asterik = "*"*int(x+(x-1))
    print(row_space+asterik)

for x in range(rows -1,0,-1):
    if x<=0:
        continue
    row_space =  ' ' * (rows - x)
    asterik = "*"*int(x+(x-1))
    print(row_space+asterik)