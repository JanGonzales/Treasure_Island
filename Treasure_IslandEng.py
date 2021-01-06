print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Player = input("You are in a cross road, do you want to go left or right? ")
Player = Player.lower()

if Player == "left":
  Player = input("After walking you notice a lake and in the middle of that lake is a house\n" + "Choose: Swim or Ignore and continue walking.")
  Player = Player.lower()
  if Player == "swim":
    Player = input ("Exhausted and hungry, you've finally reached the house. In front is a wooden door with three varying colours one is Red, Blue and Green. Choose:  ")
    Player = Player.lower()
    if Player == "red":
      print("Burned by fire. GAME OVER!")
    elif Player == "blue":
      print("Eaten by the beast. GAME OVER!")
    elif Player == "yellow":
      print ("Treasure! You have finally found it!")
    else:
      print("Wrong choice")
  else:
    print("You where attacked by a troll and was smashed into a pulp GAME OVER!")
else:
  print("You've chosen the wrong path and fell into a hole never to be seen again...")
  print("""      )        
      ()        
     ,/.        
     |:|        
     |'|        
     | |        
     | |        
    ,---''.     
  ,'    ,. :.   
 |     (  )':.  
 |      `' .\ \ 
  \   '.   '.'| 
   '--.  "-.-". 
  [lf] -.___.,'""")