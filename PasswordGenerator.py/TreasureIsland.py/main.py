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

print()
print()
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You wake up on an island not sure what to make of it. You decide: ")
direction = input("Do you go left or right: ").lower()

if direction == 'left':
    print("After walking for a mile you get to a river, but you notice it's too wide to attempt a cross over: ")
    swimOrWait = input("What to do next? Wait or try and swim over: ").lower()

    if swimOrWait == 'wait':
        print("Good idea to wait. A stranger gives you a ride into town.")
        colour = ""
        while colour not in ["red", "yellow", "blue"]:
            colour = input("You are dropped off at a wall with 3 colors: (RED | YELLOW | BLUE): ").lower()
        if colour == 'red':
            print("Burned by fire.")
            print("GAME OVER")
        elif colour == "blue":
            print("Eaten by beasts.")
            print("GAME OVER")
        elif colour == 'yellow':
            print("You won!")
            print("Congratulations, you found the treasure!")
    else:
        print("You decided to swim and were eaten alive by a whale.")
        print("GAME OVER")
else:
    print("Deciding to go right caused you to fall off a mountain.")
    print("GAME OVER")
