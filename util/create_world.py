from django.contrib.auth.models import User
from Lambda_Mud.models import Player, Room
from util.sample_generator import World

Room.objects.all().delete()
r_outside = Room(title="Outside Cave Entrance", description="North of you, the cave mount beckons.")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. You spot a secret passage leading east.""")

r_passage = Room(title="Secret Passage", description="""The secret passage is pitch-black in darkness.  
You light a torch to guide your way as it bends to move north, another path leading south, back towards the way you came.""")

r_passage_s = Room(title="Secret Passage", description="""The path continues southward, 
until eventually you begin to see light shining from the mouth of the cavernous passage.""")

r_passage_n = Room(title="Secret Passage", description="""Continuing north, you see a door made of rotting boards of wood, 
leading west, and presumably, towards the thieves.""")

r_hideout = Room(title="Thieves' Hideout", description="""It seems the thieves are using the room behind the door as a makeshift hideout, or at least were.
They seem to have moved out, and you see yet another cavernous path to the west.""")

r_mineshaft = Room(title="Mineshaft", description="""Continuing west, you find yourself traveling into a mineshaft, abandoned carts and pickaxes indicating 
it hasn't been used for it's original purpose in years.  The path continues west.""")

r_dwarfruins = Room(title="Dwarven Ruins", description="""You emerge from the mineshaft into what must be dwarven ruins from an age long-past.
You hear shouting to the north, though the main fortress of the ruin lies further to the west, and a strange light is seen to the south.""")

r_thieves = Room(title="Trapped Room", description="""You head towards the shouting, only to find the end of the carnage, various men, presumably the thieves,
dead to a variety of fiendish traps.  The only way is back to the ruins.""")

r_boatmurdered = Room(title="Boatmurdered", description="""For some reason, this dwarven ruin is filled to the brim with lava and elephant bones.  
The only way is back to the ruins.""")

r_excalibur = Room(title="Axe in the Stone", description="""You find the source of the glowing, an axe lodged into the stone of the wall.  Try as you might,
 however, you cannot seem to pull it from it's place.  The only way is back to the ruins.""")

r_exit = Room(title="Passage Exit", description="""You exit into the bright sunlight of the forest, foliage covering the passage from all but the most 
well-trained eyes.  You have paths leading east, west, and south.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_passage.save()
r_passage_s.save()
r_passage_n.save()
r_hideout.save()
r_dwarfruins.save()
r_thieves.save()
r_boatmurdered.save()
r_excalibur.save()
r_exit.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_passage, "w")
r_passage.connectRooms(r_treasure, "e")

r_passage.connectRooms(r_passage_s, "s")
r_passage_s.connectRooms(r_passage, "n")

r_passage.connectRooms(r_passage_n, "n")
r_passage_n.connectRooms(r_passage, "s")

r_passage_n.connectRooms(r_hideout, "w")
r_hideout.connectRooms(r_passage_n, "e")

r_hideout.connectRooms(r_mineshaft, "w")
r_mineshaft.connectRooms(r_hideout, "e")

r_mineshaft.connectRooms(r_dwarfruins, "w")
r_dwarfruins.connectRooms(r_mineshaft, "e")

r_dwarfruins.connectRooms(r_thieves, "n")
r_thieves.connectRooms(r_dwarfruins, "s")

r_dwarfruins.connectRooms(r_boatmurdered, "w")
r_boatmurdered.connectRooms(r_dwarfruins, "e")

r_dwarfruins.connectRooms(r_excalibur, "s")
r_excalibur.connectRooms(r_dwarfruins, "n")

r_passage_s.connectRooms(r_exit, "s")
r_exit.connectRooms(r_passage_s, "n")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()


w = World()
num_rooms = 44
width = 8
height = 7
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
