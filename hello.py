import random
def guesser(x):
	while True:
		y=int(input("Guess a number from 1 to 10: "))
		if x!=y:
			print("Guess again!")
		else:
			break
	print("Jackpot!")
x = random.randint(1,10)
guesser(x)
