from ssquerier import Participant
from random import randint, choice

if __name__ == "__main__":
	temp = Participant(1,2,3,4,5)
	val = temp.mod_pow(100,20, 175)
	print val