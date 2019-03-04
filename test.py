from ssquerier import Participant
from ssquerier import distribute_shares
from random import randint, choice
from rsa import test_prime

if __name__ == "__main__":
	for i in range(10):
		p = randint(3, 100)
		print p, test_prime(p, 4**-5)