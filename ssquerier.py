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
		

	# This function simulates a participant querying all other participants to see whether
	# or not they can recover the secret
	def query_participants(self, all_participants, query):
	
	# val: the secret
	# k: the number of valid participant shares needed to recover the secret
	# q: the prime you mod by as you'll be working in mod q
	def distribute_shares(all_participants, val, k, q):
	
	# computes the greatest common divisor of a and b
	def gcd(a, b):
	
	# computes b to the p-th power mod q
	# must be done in logarithmic time complexity
	# note: don't do b ** p % q; this could overflow with very large numbers
	def mod_pow(b, p, q):
	
	# computes the inverse of x mod q
	def inverse(x, q):
	