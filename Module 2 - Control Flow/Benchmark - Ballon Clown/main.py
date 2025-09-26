sword = 5
dog = 7
triforce = 11
current_capacity = 0
print('I can make a sword, dog, or the triforce.')
balloon_type = input('Which balloon do you want? ')

while True:
    if balloon_type == "sword":
        print('Balloon:',balloon_type)
        print('Capacity:',sword)
        print("Current:",current_capacity)
        options = input('[pump] air, [release] air, [tie] balloon> ')
        if options == 'pump':
            current_capacity += 3
            if current_capacity > sword:
                print('POP!')
                break
        if options == 'release':
                current_capacity -= 2
                if current_capacity < 0:
                      current_capacity=0
        if options == "tie":
                print('Here is your',balloon_type,'balloon!')
                break
    if balloon_type == "dog":
        print('Balloon:',balloon_type)
        print('Capacity:',dog)
        print("Current:",current_capacity)
        options = input('[pump] air, [release] air, [tie] balloon> ')
        if options == 'pump':
            current_capacity += 3
            if current_capacity > dog:
                print('POP!')
                break
        if options == 'release':
                current_capacity -= 2
                if current_capacity < 0:
                    current_capacity=0
        if options == "tie":
                print('Here is your',balloon_type,'balloon!')
                break
    if balloon_type == "triforce":
        print('Balloon:',balloon_type)
        print('Capacity:',triforce)
        print("Current:",current_capacity)
        options = input('[pump] air, [release] air, [tie] balloon> ')
        if options == 'pump':
            current_capacity += 3
            if current_capacity > triforce:
                print('POP!')
                break
        if options == 'release':
                current_capacity -= 2
                if current_capacity < 0:
                    current_capacity=0
        if options == "tie":
                print('Here is your',balloon_type,'balloon!')
                break
