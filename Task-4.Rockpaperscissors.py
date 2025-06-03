import random

options = ("rock", "paper", "scissors")
player_score=0
comp_score=0

while True:
    player=None
    computer=random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score+=1
        print("player score: ", player_score)
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score+=1
        print("player score: ", player_score)
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score+=1
        print("player score: ", player_score)
    else:
        print("You lose!")
        comp_score+=1
        print("computer score: ", comp_score)
    play_again=input("\nPlay again? (y/n): ").lower()

    if play_again != 'y':
        print("\nThanks for playing!")
        break

        

    
    
    
    
