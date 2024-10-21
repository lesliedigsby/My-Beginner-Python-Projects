import random

options = ["rock", "paper", "scissors"]

running = True

while running:

    player_choice = None
    computer_choice = random.choice(options)

    while player_choice not in options:
        player_choice = input("Enter a choice (Rock, paper, or scissors): ")


    print(f"Player chose: {player_choice}")
    print(f"The computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")