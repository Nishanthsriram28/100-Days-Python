import random
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
print("Welcome to Rock, Paper, Scissors. ")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player_choice = int(input())
computer_choice = random.randint(0,2)
RPS_list = [rock,paper,scissors]

if player_choice == 0:
    print("Your Choice : Rock",RPS_list[player_choice])
elif player_choice == 1:
    print("Your Choice : Paper", RPS_list[player_choice])
elif player_choice == 2:
    print("Your Choice : Scissors", RPS_list[player_choice])
else:
    print("Not a valid input, You lose!")


if computer_choice == 0:
    print("Computer Choice : Rock", RPS_list[computer_choice])
elif computer_choice == 1:
    print("Computer Choice : Paper", RPS_list[computer_choice])
elif computer_choice == 2:
    print("Computer Choice : Scissors", RPS_list[computer_choice])


if player_choice < 0 and player_choice > 2:
    print("It's an invalid number. You lose !")
elif(player_choice == computer_choice):
    print("It's a draw")
elif player_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You Win")

elif player_choice == 1:
    if computer_choice == 2:
        print("You lose")
    else:
        print("You Win")

elif player_choice == 2:
    if computer_choice == 0:
        print("You lose")
    else:
        print("You Win")





