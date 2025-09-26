# Predefined list of songs
songs = [
    ["Bohemian Rhapsody", "Queen", ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"], "A Night at the Opera", 354, True],
    ["Shape of You", "Ed Sheeran", [], "÷ (Divide)", 233, True],
    ["Someone Like You", "Adele", [], "21", 285, False],
    ["Happy", "Pharrell Williams", [], "Girl", 233, False],
    ["Uptown Funk", "Mark Ronson ft. Bruno Mars", [], "Uptown Special", 270, True],
    ["Billie Jean", "Michael Jackson", [], "Thriller", 292, True]
]



print('Menu:\n1. Add a new song\n2. Remove a song by title\n3. View all songs by favorites\n4. View all songs by artist\n5. Update a song\n6. Exit')
while True:
    options = input("Enter your choice (1-6): ")
    if options == "1":
        print('Adding a new song...')
        song = input('Enter the title: ')
        artist = input('Enter the primary artist name: ')
        association = input("Enter associated artists (comma-separated): ")
        album = input("Enter the album title: ")
        time = input('Enter the duration in seconds: ')
        fav = input("Is it a favorite song? (y/n): ")
        if fav == "y":
            add= [song, artist,association, album,time,True]
            songs.append(add)
        else:
            add= [song, artist,association, album,time,False]
            songs.append(add)
        print(f"Song '{song}' added successfully!")

    elif options == "2":
        remove = input("Enter the title of the song to remove: ")
        for song in songs:
            if remove == song[0]:
                songs.remove(song)

    elif options == "3":
        for x in songs:
            if x[5] == True:
                (f'Favorite Songs')
                print(f'{x[0]} by {x[1]}')

    if options == "4":
        art = input('What artist? ')
        for x in songs:
            if x[1] == art:
                print(f'{x[0]} by {x[1]}')

    if options == "5":
        update = input("Which song title? ")
        f=False
        for x in songs:
            if x[0] == update:
             f = True
             change = input("What would you like to change it to? ")
             x[0]= change
        if f == False:
            print('This song is not in your collection!')

    if options == "6":
        quit()
