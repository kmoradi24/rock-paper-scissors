import random

choices = ["rock","paper","scissors"]
choice = random.choice(choices)
user = raw_input("What do you pick: rock, paper or scissors? ")
if user == 'rock' or 'paper' or 'scissors':
    print "You have picked %s and the computer picked %s " % (user,choice)
if user == 'rock':
    if choice == 'scissors':
        print "You win!"
    elif choice == 'rock':
        print "Tie game"
    else:
        print "Computer wins"
if user == 'paper':
    if choice == 'rock':
        print "You win!"
    elif choice == 'paper':
        print "Tie Game"
    else:
        print "Computer wins"
if user == 'scissors':
    if choice == 'Rock':
        print "Computer wins"
    elif choice == 'Paper':
        print "You win!"
    else:
        print "Tie Game"
