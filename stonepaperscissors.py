#STONE PAPER SCISSORS GAME
#MADE BY ATHARVA S BHIDE
import random

print("---------------------------------------------------------")


while True:

	print("WELCOME TO THE STONE PAPER SCISSORS GAME!")

	print("TYPE START BELOW TO START THE GAME-")
	print("TYPE QUIT BELOW TO EXIT THE GAME-")

	start = input()

	if start=="START":
		list1 = ["STONE", "PAPER", "SCISSORS"]

		print("TYPE YOUR MOVE BELOW-")

		move = input()

		if move=="STONE" or move=="PAPER" or move=="SCISSORS":

			compmove = random.choice(list1)

			print("COMPUTER:", compmove)

			if move=="STONE" and compmove=="STONE":

				print("GAME TIED!")

			elif move=="STONE" and compmove=="PAPER":

				print("COMPUTER WINS!")

			elif move=="STONE" and compmove=="SCISSORS":

				print("YOU WIN!")

			elif move=="PAPER" and compmove=="PAPER":

				print("GAME TIED!")

			elif move=="PAPER" and compmove=="STONE":

				print("YOU WIN!")

			elif move=="PAPER" and compmove=="SCISSORS":

				print("COMPUTER WINS!")

			elif move=="SCISSORS" and compmove=="STONE":

				print("COMPUTER WINS!")

			elif move=="SCISSORS" and compmove=="PAPER":

				print("YOU WIN!")

			else:
				print("GAME TIED!")

		else:
			print("ERROR! PLEASE ENTER A VALID INPUT!")

	elif start=="QUIT":
		break

	else:
		print("PLEASE ENTER A VALID INPUT!")

	continue

	


	




					
					

				






	