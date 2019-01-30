
def shaman_room():
  print("You find yourself inside the cave of a mystical shaman.")
  print("The shaman grants you one wish:")
  print("\t1. Magical powers")
  print("\t2. Unlimited wealth")
  print("\t3. Look into the future")
  print("\t4. Leave")
  wish = int(input("> "))
  
  if wish == 1:
    print("Choose a power:")
    print("\t1.Flight")
    print("\t2.Invincibility")
    print("\t3.X-ray vision")
    print("\t4. You change your mind and leave.")
    power = int(input("> "))
    
    if power != 4:
      print("The shaman has granted you your wish!")
      print("Be wary traveller, with grate power comes great responsibility!")
      print("Now, begone!")
    else:
      print("Wisdom is the key to sanctity. Your choice is wise. Begone!")
  elif wish == 2:
    print("The shaman has granted you your wish!")
    print("Be conscious traveller, more money means more problems.")
    print("Now, begone!")
  elif wish == 3:
    print("Curious traveller, the future is not yet written.")
    print("Go write it yourself and do not rely on anyone else to do so! Begone!")
  else:
    print("Begone at once!")

def goblin_room():
  print("You stumbled upon dreaded room full of... small furnishing.")
  print("Beyond in the midst you see an ember creeping closer.")
  print("Behind the ember you see... green pointy ears?")
  print("Oh no! It's a band of goblin rogues!")
  print("You have no choice but to room from this room. Skram!")

def start():
  print("You wake up in a cold, wet cave 15,000 feet below the surface of the Earth.")
  print("You see a fork in the road. Do you go LEFT, RIGHT or go back to sleep?")
  path = input("> ")
  if path.lower() == "left":
    shaman_room()
  elif path.lower() == "right":
    goblin_room()
  else:
    print("Night, night! Don't let the bed bugs bite.")

start()