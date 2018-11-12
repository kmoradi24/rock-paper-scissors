import random
import sys


def start():
    while True:
        player_choice = input("Rock, Paper, or Scissors?")
        cpu_random = random.randint(1,3)
        cpu_choice = cpu_random
        if cpu_random == 1:
            cpu_choice = "Rock"
        elif cpu_random == 2:
            cpu_choice = "Paper"
        elif cpu_random == 3:
            cpu_choice = "Scissors"

## The computer chooses and then we analyze it

        def analyze():

            play_again = None
#Tie
            if player_choice == cpu_choice:
                print("Tie!")
                play_again = input("Play again?")

#Rock

            elif player_choice == "Rock" and cpu_choice == "Paper":
                print("You Lose!")
                play_again = input("Play again?")
            elif player_choice == "Rock" and cpu_choice == "Scissors":
                print("You Win!")
                play_again = input("Play again?")

#Paper

            elif player_choice == "Paper" and cpu_choice == "Scissors":
                print("You Lose!")
                play_again = input("Play again?")
            elif player_choice == "Paper" and cpu_choice == "Rock":
                print("You Win!")
                play_again = input("Play again?")

#Scissors outcome

            elif player_choice == "Scissors" and cpu_choice == "Rock":
                print("You Lose!")
                play_again = input("Play again?")
            elif player_choice == "Scissors" and cpu_choice == "Paper":
                print("You Win!")
                play_again = input("Play again?")

## Ask for round 2

            if play_again == "Yes":
                play()
            elif play_again == "No":
                print("Game Over")
                sys.exit()
            else:
                print("Please try again")
                play_again = input("play again?")
                return play_again

        compare()



#ask if player wants to start
def game_start():
    while True:
        begin = input("Would you like to play Rock, Paper, Scissors?")
        if begin == "Yes":
            play()
            return begin
        while begin != "Yes":
            if begin == "No":
                print("Game Over")
                return begin
            else:
                print("Please try again")
                break

game_start()
