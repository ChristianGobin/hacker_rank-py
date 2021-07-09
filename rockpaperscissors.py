# Rock Paper Scissors Console Game
"""
Uses Random Number Generator, User Input, Loops, Functions
Objective: Play Rock, Paper, Scissors in console against computer.
"""
import math
import random as random
def rps_game():
	user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
	possible_choices = ['rock', 'paper', 'scissors']
	computer_choice = possible_choices[math.floor(random.random() * len(possible_choices))]
	play_again = 0
	while user_choice not in possible_choices:
		user_choice = str(input("Try Again \nEnter a valid choice: ")).lower()
	while user_choice is computer_choice:
		user_choice = str(input("Try Again \nEnter a valid choice: "))
	
	# while the user does not say no
	while play_again != 'no':
		computer_choice = possible_choices[math.floor(random.random() * len(possible_choices))]
		print(computer_choice)
		while user_choice not in possible_choices:
			user_choice = str(input("Try Again \nEnter a valid choice: ")).lower()
		while user_choice is computer_choice:
			user_choice = str(input("Try Again \nEnter a valid choice: "))
		if((user_choice == 'scissors') and (computer_choice == 'paper')):
			print("You win\t")
			play_again = str(input("Play Again?: "))
			user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
			
		elif((user_choice == 'scissors') and (computer_choice == 'rock')):
			print("You lose\t")
			play_again = str(input("Play Again?: "))
			user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
			
		elif((user_choice == 'paper') and (computer_choice == 'rock')):
			print("You win\t")
			play_again = str(input("Play Again?: "))
			user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
			
		elif((user_choice == 'paper') and (computer_choice == 'scissors')):
			print("You lose\t")
			play_again = str(input("Play Again?: "))
			user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
			
		elif((user_choice == 'rock') and (computer_choice =='paper')):
			print("You lose\t")
			play_again = str(input("Play Again?: "))
			user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
			
		elif((user_choice == 'rock') and (computer_choice =='scissors')):
			print("You win\t")
			play_again = str(input("Play Again?: "))
			user_choice = str(input("1,2,3 Shoot: (Enter Your Choice)\n")).lower()
			
		
"""
possible outcomes:
s, s
p, p
r, r
s,p
s,r,
p,s,
p,r,
r,p
r,s

"""
	
	
rps_game()