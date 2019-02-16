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
		for j in range(len(points)):
			y = points[j][1]
			l = basis(points, self.share[0], j)
			v += y*l
		v = v % q
		return self.mod_pow(self.g, v, self.p)

	# jth basis at x 
	def basis(points, x, j):
		val = 1
		for m in range(len(points)):
			if not m == j:
				a = (x - points[m][0]) 
				b = (points[j][0] - points[m][0])
				v=Fraction(a)/Fraction(b)
				val *= v
		return val


	# This function simulates a participant querying all other participants to see whether
	# or not they can recover the secret
	def query_participants(self, all_participants, query):
		


	# val: the secret
	# k: the number of valid participant shares needed to recover the secret
	# q: the prime you mod by as you'll be working in mod q
	def distribute_shares(self, all_participants, val, k, q):
		r = 1000
		neg = [1, -1]
		coefs = [choice(neg) * Fraction(randint(1, r), randint(1, r)) for i in range(0, k-1)]
		coefs.insert(0, val)

		xs = []
		ys = []
		for i in range(k):
			p = 0
			while p == 0 or p in xs:
				p = randint(-r, r)

			xs.append(p)
			ys.append(polyVal(coefs, p) % q) #?
		
		keys = [(xs[i], ys[i]) for i in range(len(xs))]

		for i in range(len(all_participants)):
			all_participants[i].share = keys[i]

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
	def gcd(self, a, b):
		r = a % b
		if r == 0:
			return b
		else:
			return self.gcd(b, r)

	# computes b to the p-th power mod q
	# must be done in logarithmic time complexity
	# note: don't do b ** p % q; this could overflow with very large numbers
	def mod_pow(self, b, p, q):
		total = 1
		current = b
		for bit in bin(p)[2::][::-1]: #for bit in binary of p from lsb->msb
			if bit == '1':
				total = (total * current) % q
			current = (current ** 2) % q
		return total

	# computes the inverse of x mod q
	def inverse(self, x, q):
		return self.mod_pow(x, q-2, q)