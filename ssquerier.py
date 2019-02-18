from fractions import Fraction
from random import randint, choice

class Participant:
	
	# This function is called when a participant is first initialized
	# Each participant will have its own p, q, a, g, and share
	# p: a largish prime number
	# q: also a largish prime number
	# a: p = aq + 1
	# g: a generator number
	# share: a share in the form (x, y)
	def __init__(self, p, q, a, g, share):
		self.p = p
		self.q = q
		self.a = a
		self.g = g
		self.share = share
	
	# This function is in charge of interpolating the shares of all participants
	# with regard to self (i.e self.share[0] will be the x-coordinate you interpolate at)
	# Calculate some variable v and indicator function I such that v = (I(x) * y) mod q
	# Returns (g ** v) mod p
	def partial_interpolate(self, all_participants):
		points = [p.share for p in all_participants]
		v = 0
		print "keys2: ", points
		for j in range(len(points)):
			y = points[j][1]
			l = self.basis(points, self.share[0], j)
			v += y*l
		v = v % self.q
		return mod_pow(self.g, v, self.p)

	# jth basis at x 
	def basis(self, points, x, j):
		val = 1
		for m in range(len(points)):
			if not m == j:
				a = x - points[m][0]
				b = points[j][0] - points[m][0]
				
				if b == 0:
					print "\nFUCK: ", points[j][0], points[m][0], " || ", j, m
				else: 
					v = Fraction(a)/Fraction(b)
					val *= v
		return val


	# This function simulates a participant querying all other participants to see whether
	# or not they can recover the secret
	def query_participants(self, all_participants, query):
		secret = self.partial_interpolate(all_participants)
		
		actual = self.g ** (secret * self.a)
		actual = actual % self.p

		guess = self.g ** (query * self.a)
		guess = guess % self.p

		print actual, guess

		return actual == guess


# val: the secret
# k: the number of valid participant shares needed to recover the secret
# q: the prime you mod by as you'll be working in mod q
def distribute_shares(all_participants, val, k, q):
	print "sec: ", val
	r = 1000
	neg = [1, 1] #################
	coefs = [choice(neg) * Fraction(randint(1, r), randint(1, r)) for i in range(0, k-1)]
	coefs.insert(0, val)

	keys = set([])
	
	while len(keys) < len(all_participants):
		p = randint(1, r)
		fp = polyVal(coefs, p)
		keys.add((p % q, fp % q))

	print "keys1: ", keys

	for i in range(len(all_participants)):
		all_participants[i].share = keys.pop()

# given list of coefficents for p, find p(x)
def polyVal(coefs, x):
	val = 0
	i = 0
	for c in coefs:
		val += c * (x**i)
		i += 1
	return val

# computes the greatest common divisor of a and b
# Euclidian algorithm
def gcd(a, b):
	r = a % b
	if r == 0:
		return b
	else:
		return gcd(b, r)

# computes b to the p-th power mod q
# must be done in logarithmic time complexity
# note: don't do b ** p % q; this could overflow with very large numbers
def mod_pow(b, p, q):
	total = 1
	current = b

	binary = bin(int(p))
	binary = binary[2:]
	binary = binary[::-1]

	for bit in binary:
		if bit == '1':
			total = (total * current) % q
		current = (current ** 2) % q
	return total

# computes the inverse of x mod q
def inverse(x, q):
	if q == 1:
		return 0

	for i in range(1, q):
		if (i * x) % q == 1:
			print i
			return i

	return None