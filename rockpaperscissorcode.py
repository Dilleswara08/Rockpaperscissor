import random

choices=["rock", "paper", "scissors"]

player_choice= input("choose rock, paper, or scissors: ")
computer_choice= random.choice(choices)

print(f"You choose {player_choice}, and the computer chose {computer_choice}.")

if player_choice == computer_choice:
    print("It's a tie!")
elif(player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")