power = "Off"
volume = 0
sound = "Bright White"


print(f"Power: {power}")

while True:
    user = input("> ")
    if user == "P":
        if power == "Off":
            power = "On"
        else:
            power = "Off"
    elif user == "V+":
        volume += 10
        if volume > 100:
            volume = 100
    elif user == "V-":
        volume -= 10
        if volume < 0:
            volume = 0
    elif user == "S":
        if sound == "Bright White":
            sound = "Deep White"
        elif sound == "Deep White":
            sound = "Ocean Surf"
        elif sound == "Ocean Surf":
            sound = "Bright White"
    elif user == "quit":
        break

    print(f"Power: {power}")
    if power == "On":
        print(f'Volume: {volume}')
        print(f'Noise: {sound}')