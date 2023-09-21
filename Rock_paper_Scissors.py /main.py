import random

# Password Generator Project
rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]

while True:

    print("Welcome to [ROCK PAPER SCISSORS]")
    user_choice = int(input("Select 0 for rock, 1 for paper, 2 for scissors or q to quit: \n"))

    try:
        user_choice = int(user_choice)
        if 0 > user_choice > 2:
            print("Invalid input. Please select 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please select 0, 1, or 2.")
        continue

    cpu_choice = random.randint(0, 2)
    print(game_options[user_choice])

    if user_choice == cpu_choice:
        print("Its a Tie ..")

    elif ((user_choice == 0 and cpu_choice == 2) or
        (user_choice == 1 and cpu_choice == 0) or
        (user_choice == 2 and cpu_choice == 1)):

            else:
                print("Computer Wins")


