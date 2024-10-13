import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Hand = [rock, paper, scissors]

player = int(input("Please type [0] for rock, [1] for paper, and [2] for scissors:  "))
computer = random.randint(0, 2)

if player == computer:
    print(f"You choose:\n{Hand[player]}\n")
    print(f"Computer choose\n{Hand[computer]}\n")
    print("Its a Draw!")
elif player == 0:
    if computer == 1:
        print(f"You choose:\n{Hand[player]}\n")
        print(f"Computer choose\n{Hand[computer]}\n")
        print("You Lose!")
    else:
        print(f"You choose:\n{Hand[player]}\n")
        print(f"Computer choose\n{Hand[computer]}\n")
        print("You Win!")
elif player == 1:
    if computer == 2:
        print(f"You choose:\n{Hand[player]}\n")
        print(f"Computer choose\n{Hand[computer]}\n")
        print("You Lose!")
    else:
        print(f"You choose:\n{Hand[player]}\n")
        print(f"Computer choose\n{Hand[computer]}\n")
        print("You Win!")
elif player == 2:
    if computer == 0:
        print(f"You choose:\n{Hand[player]}\n")
        print(f"Computer choose\n{Hand[computer]}\n")
        print("You Lose!")
    else:
        print(f"You choose:\n{Hand[player]}\n")
        print(f"Computer choose\n{Hand[computer]}\n")
        print("You Win!")
else:
    print("Oops... wrong input! Please input number between 0 - 2")