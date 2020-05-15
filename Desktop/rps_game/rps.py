import random

options = ['rocks', 'papers', 'scissors','rock','paper','scissor','r','s','p']
rocks 	= ['rock' , 'rocks','r']
scissors= ['scissor','scissors','s']
papers  = ['paper', 'papers','p']
p_score = 0
c_score = 0
while True:
	try:
		print()
		print("Player".ljust(10),":",p_score)
		print("Computer".ljust(10),":",c_score)
		op = random.randint(0,2)
		player = input("Player-----").lower()
		computer = options[op]
		print("Computer---"+computer)

		if player in rocks and computer == 'papers':
			print("computer wins")
			c_score += 1
		elif player in rocks and computer == 'scissors':
			print("player wins")
			p_score += 1
		elif player in scissors and computer == 'rocks':
			print("computer wins")
			c_score += 1
		elif player in scissors and computer == 'papers':
			print("player wins")
			p_score += 1
		elif player in papers and computer == 'rocks':
			print("player wins")
			p_score += 1
		elif player in papers and computer == 'scissors':
			print("computer wins")
			c_score += 1
		elif player not in options :
			print("enhi taiya jhulni hai rani ho rama")
			c_score += 5
		else:
			print("Draw")
	except :
		print("Finish")