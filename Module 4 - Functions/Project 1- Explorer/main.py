def subnautica():
    print("""Your ship, the Aurora, crashes on planet 4546B due to a powerful energy pulse from the planet's Quarantine Enforcement Platform. 
This pulse cripples the ship, destroying most of the life pods and causing a fiery crash into the ocean.
Yours and 24 other life pods that were successfully ejected are shot into the waters.
After being unconscious for three hours by impact with an internal loose panel, you finally awaken and step outside of your pod, able to see the Aurora flaming and nose-dived into the vast waters.
You dive into the waters below, seeing many strange creatures swim past you. 
Some of them have similarities to creatures on earth while others seem to be otherworldly... probably because they are.
You see a biome where the water is a murky green with an expanse of kelp, which you have given the name the 'Kelp Forest'. 
There are more creatures that you have not encountered in this area, along with resources you may need.
On the other side, you see an open biome you have dubbed the 'Grassy Plateaus'.
It is characterized by large, pillar-like structures seemingly created from water current erosion, smooth marine plains, and sandy terrain almost completely carpeted with Blood Grass, giving the Grassy Plateaus their distinctive name.
After completely exploring the nearby area you have dubbed as the 'Safe Shallows', you realize the resources here will not sustain here forever. You decide to move on for now.
\nWhere would you like to go?
1.Kelp Forest
2.Grassy Plateaus
or press q to quit""")
    options = input('> ')
    if options == "kelp forest":
        kelp()
    elif options == "grassy plateaus":
        grassy()
    elif options == "q":
        quit
    else:
        print("This is not a valid location.")
#break so i can see for some reason .lower isn't working so user has to enter in lowercase
def shallows():
    print("You return to the safe shallows, and its the exact same as before. The Aurora is still burning in the distance.")
    print("\nWhere would you like to go?\n1.Kelp Forest\n2.Grassy Plateaus\n or press q to quit")
    options = input('> ')
    if options == "kelp forest":
        kelp()
    elif options == "grassy plateaus":
        grassy()
    elif options == "q":
        quit
    else:
        print("This is not a valid location.")
#break so i can see
def kelp():
    print("""You swim to the Kelp Forest, a biome characterized by the abundance of Creepvine plants, giving it a distinct greenish hue.
It's a relatively safe and resource-rich area, and is home to various passive lifeforms, with the exception of Stalkers and Drooping Stingers. 
You swim around the vines and collect various resources, avoiding run-ins with the local aggressive fauna. There's not much here and after about an hour you decide to move on.
You can only return to the Safe Shallows
\nWhere would you like to go?\n1.Safe Shallows\nor press q to quit""")
    options = input("> ")
    if options == "safe shallows":
        shallows()
    if options == "q":
        quit
    else:
        print('You cannot go here!')
#break so i can see
def grassy():
    print("""You swim to the open expanse of the Grassy Plateaus, the ground covered in bright red sea grass where various creatures hide.
In the distance you see a suspicious cloud of dust and swim over. To your despair, it appears to be a sand shark in the middle of burying itself.
The Sand Shark's body is segmented and its dorsal surface is completely covered with a plated exoskeleton, having a grayish-violet upper side and a pinkish underbelly, with a brief gap where its muscle can be seen.
Short, grey, leg-like appendages appear in two rows of six on its underside, used to disturb the surface of the sand. 
The Sand Shark's head features four orange eyes, which are divided into sets of two on each side, and a large fin-like protrusion on the top.
It has a rather large mouth equipped with six rows of sharp, jagged teeth, which continue to go down the Sand Shark's throat.
\nIt growls as it spots you, giving you just a few second to get away.
You take the opportunity gratefully as you flee, the creature returning to its current task of burying itself.
You spend a few hours exploring the biome when you come across another life pod sitting on the seafloor. you have some hope in your chest that maybe you aren't alone, but that hope quickly decimates as you get a closer look at the pod. 
It has a hole blown through the top, but the explosion seems to have come from inside...
You find the data bank in the decimated pod, and hook it into your playback device.
CREW: Ma'am, I need you to stay calm. We're not in immediate danger.\nPASSENGER: Where are the rescue teams?!\nCREW: The Aurora didn't make it.\nPASSENGER: So where are the rescue teams?!\nCREW: They're dead, ma'am. We have rendezvous coordinates, but the route's irradiated.\nPASSENGER: So what are you going to do?!\nCREW: I'm head of human resources, ma'am. This is not my expertise. But the PDA says if we can find some lead we can make radiation suits.\nPASSENGER: Out there? I am not setting foot outside this life pod without the proper protection.\nCREW: Don't worry. I'll go.
The machine goes quite for a moment before continuing, the second recording recording about 4 hours later...
CREW: What are you doing?!\nPASSENGER: You were gone so long, I thought you'd drowned.\nCREW: Put the flare down!\nPASSENGER: I was going to try and attract someone's attention.\nCREW: That's not a distress flare! Stop waving it around like that, you'll catch the fuel line!\n *Explosion*
You sit for a moment in silence, a heavy ache in your heart before deciding to move on. You cannot sit and stare at your wounds forever. It won't keep you alive, that's for sure.
You finally decide to move on. You have two new biomes to explore, or you can go back to the shallows if you wish.
One biome known as the Sparse Reef seems to live up to its name, the area mostly flat with different kind of corals scattered around.
The area seems mostly safe, the fauna here no bigger than anything in the Safe Shallows.
The other biome is the complete opposite. Known as 'The Dunes', it feature vast, sandy plains and dunes, sometimes littered with various types of rock structures.
It is also home to many dangerous types of Fauna, the most notable one being the eight Reaper Leviathans that patrol the open spaces of the biome.
\nWhere would you like to go?\n1.Sparse Reef\n2.Dunes\n3.Safe Shallows\n or press q to quit""")
    options = input("> ")
    if options == "sparse reef":
        reef()
    elif options == "dunes":
        dunes()
    elif options == "safe shallows":
        shallows()
    elif options == "q":
        quit
    else:
        print("You cannot go here!")
#break so i can see
def dunes():
    print("""You continue on into the Dunes despite your acknowledgement of the dangers and little resources. It seems you have a death wish. 
As you carry on into the depths where you can hardly see for what feels like hours, you hear a roar coming from behind you.
Suddenly, something grabs your Prawn suit and flings you around, dealing a significant amount of damage. The Reaper Leviathan that attacked you continues its ruthless pursuit, but you manage to escape, hiding behind some measly seafloor rocks.
\nWhere would you like to go?\n 1. Grassy Plateaus\nor press q to quit""")
    options = input("> ")
    if options == "grassy plateaus":
        grassy()
    elif options == "q":
        quit
    else:
        print("You cannot go here!")
#break so i can see
def reef():
    print("""The Sparse Reef is a large, sprawling region composed of relatively flat areas covered by green mounds scattered with Table Coral as well as large fissures where most of the bioluminescent flora inhabit, notably the Eye Stalks.
Some areas have deep drop-offs, along with basins, caves, and other irregular formations. A green-blue fog can be seen shrouded over the distinctively unsaturated landscape, creating a gloomy, desolate atmosphere.
As you swim around, you collect various debris and samples, hoping to use some of it to help you get home. You can only return to the Safe Shallows.
\nWhere would you like to go?\n1. Safe Shallows\nor press q to quit""")
    options = input("> ")
    if options == "safe shallows":
        shallows()
    elif options == "q":
        quit
    else:
        print("You cannot go here!")
    

 
subnautica()