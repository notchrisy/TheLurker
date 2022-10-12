from random import randint

xLimit= 10;
yLimit= 10;

xPos= randint (0, xLimit)
yPos= randint (0, yLimit)

Keys = 0;
Flashlight = 0;
Shoes = 0;

def printInv():
  global Keys
  global Flashlight
  global Shoes
  print(">>Your current inventory is \r\nKeys = " + str(Keys) + "\r\nFlashlights = " + str(Flashlight) + "\r\nShoes = " + str(Shoes))
  userInput()

current_hp = 100;

print(
" _____ _            _                _             "
"\r\n|_   _| |          | |              | |            "
"\r\n  | | | |__   ___  | |    _   _ _ __| | _____ _ __ "
"\r\n  | | | '_ \ / _ \ | |   | | | | '__| |/ / _ \ '__|"
"\r\n  | | | | | |  __/ | |___| |_| | |  |   <  __/ |   "
"\r\n  \_/ |_| |_|\___| \_____/\__,_|_|  |_|\_\___|_|   \r\n")

name=input(">>Please enter your username: ")

def Intro1():
  print("Sarah: Hello there " + name + ", you've been asleep for a few hours now.")
  answer1=input("a: Where am I?" + "\r\nb: Who are you?" + "\r\n> ")
  if answer1 == "a":
    print("Sarah: You are in Meanwood, about 30 miles away from Vinehusk the main city")
    Intro2()
  elif answer1 == "b":
    print("Sarah: My name is Sarah, I live not to far away from here. Just on the other side of the woods.")
    Intro2()
  else:
    print(">>Unknown command, please try again.")
    Intro1()

def Intro2():
  answer2=input("a: How did I get here?" + "\r\nb: How did you find me?" + "\r\n> ")
  if answer2 == "a":
    print("Sarah: I'm not sure, I found you here uncontious 15 minutes ago.")
    userInput()
  elif answer2 == "b":
    print("Sarah: I was on my daily walk, picking the berries for my pies.")
    userInput()
  else:
    print(">>Unknown command, please try again.")
    Intro2()

def userInput():
  command=input(">>What do you want to do? Type ? for help. ")
  if "walk" in command:
    getDirection(command)
  elif "inv" in command:
    printInv()
    userInput()
  elif "health" in command:
    print("Current HP: " + str(current_hp))
    userInput()
  elif "pos" in command:
    printCoords()
    userInput()
  elif "?" in command:
    print(">>Commands are; walk (north, east, south, west), pos, inv, health and hint")
    userInput()
  else:
    print(">>Unknown command, please try again.")
    userInput()

def getDirection(command):
  if "north" in command:
    walkNorth()
  elif "south" in command:
    walkSouth()
  elif "east" in command:
    walkEast()
  elif "west" in command:
    walkWest()
  else:
    print(">>Unknown command, please try again.")
    userInput()

def walkNorth():
  global yPos

  if yPos < 100:
    print(">>You walk north...")
    yPos += 1
    userInput()
  else:
    print("\r\n>>Some sort of invisible barrier prevents you from walking any further in this direction.")
    userInput()

def walkSouth():
  global yPos

  if yPos > 0:
    print(">>You walk south...")
    yPos -= 1
    userInput()
  else:
    print("\r\n>>Some sort of invisible barrier prevents you from walking any further in this direction.")
    userInput()

def walkEast():
  global xPos

  if xPos < 100:
    print(">>You walk east...")
    xPos += 1
    userInput()
  else:
    print("\r\n>>Some sort of invisible barrier prevents you from walking any further in this direction.")
    userInput()
  
def walkWest():
  global xPos

  if xPos > 0:
    print(">>You walk west...")
    xPos -= 1
    userInput()
  else:
    print("\r\n>>Some sort of invisible barrier prevents you from walking any further in this direction.")
    userInput()

def printCoords():
  global yPos
  global xPos
  print("\r\n>>Current Position : X=" + str(xPos) + ", Y=" + str(yPos))

  event = randint(1, 20)
  if event == 5:
    global Shoes
    global current_hp
    if Shoes == 1:
      print("Thank god for these shoes!")
      Shoes = Shoes - 1
      userInput()
    else:
      current_hp = current_hp - 10
      print(">>Ouch, you stood in some glass")
      print(">>Current HP: " + str(current_hp))
      userInput()
  elif event == 10:
    global Flashlight
    if Flashlight < 3:
      Flashlight = Flashlight + 1
      print(">>You found a flashlight, type hint if you wish to use it")
      userInput()
    else:
      userInput()
  elif event == 17:
    if Shoes < 1:
      Shoes = Shoes + 1
      print(">>You have found some shoes, no need to worry about glass anymore")
    else:
      print("")
  else:
    print("")


Intro1()