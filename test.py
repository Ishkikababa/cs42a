#from ssquerier import Participant
from random import randint, choice

if __name__ == "__main__":
	totalGuesses = 0
	numGames = 10000

	for t in range(numGames):
		num = randint(0, 63)
		spotsLeft = range(64)
		guess = -1
		while not guess == num:
			guess = choice(spotsLeft)
			spotsLeft.remove(guess)
			totalGuesses += 1

	print(float(totalGuesses) / numGames)

#	temp = Participant(1,2,3,4,5)
#	val = temp.gcd(100,175)
#	print val