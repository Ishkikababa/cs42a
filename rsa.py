from random import randint
import pickle

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
			return i

	return None

# Test the primality of p.
# The chance of p not being prime should be less than chance_false.
# Should be an implementation of the Miller-Rabin primality test.
def test_prime(p, chance_false):
	s = 0
	d = p-1

	# find s,d s.t. 2^s * d = p-1
	while d%2==0:
		s += 1
		d /= 2

	failedTest = False
	k = 0

	# while (not accurate enough) and (haven't found a bad 'a')
	while 4**-k > chance_false and not failedTest:
		k += 1
		a = randint(2, p-1)
		foundBadD = not (mod_pow(a, d, p) == 1 or mod_pow(a, d, p) == p-1)
		
		# check a^(2^r * d), r from 1 to s-1
		foundGoodR = False	
		for r in range(1, s):
			n = mod_pow(a, d*(2**r), p)
			if (n == p-1): 
				foundGoodR = True
		
		if foundBadD == True and foundGoodR == False:
			failedTest = True

	return not failedTest

# encrypts message m using the public key kpub
# returns a numerical ciphertext.
def encrypt(m, kpub):
	return mod_pow(m, kpub[1], kpub[0])

# Decrypt a ciphertext c using the private key kpriv
# Returns a numerical plaintext message.
def decrypt(c, kpriv):
	return mod_pow(c, kpriv[2], kpriv[0])

# Generate a private and public key pair in the format described above.
# return a list [private, public]
def key_gen(keylength):
	kpub = []  # n, e
	kpriv = [] # n, e, d, p, q, d mod(p-1), d mod(q-1), inverse(p, q), inverse(q, p)

	l, h = 10**(keylength/2), 100**(keylength/2)
	p, q = 1,1
	while p == q:
		p,q = get_prime(l,h),get_prime(l,h)

	n = p*q

	kpub.append(n)
	kpriv.append(n)

	e = randint(1, p)
	d = inverse(e, (p-1)*(q-1))

	while (not (gcd(e, (p-1)*(q-1)) == 1)) or (not (gcd(d, (p-1)*(q-1)) == 1)):
		e = randint(1, l)
		d = inverse(e, (p-1)*(q-1))
	
	kpub.append(e)
	kpriv.append(e)

	kpriv.append(d)

	kpriv.append(p)
	kpriv.append(q)
	kpriv.append(d % (p-1))
	kpriv.append(d % (q-1))
	kpriv.append(inverse(p, q))
	kpriv.append(inverse(q, p))

	#print kpriv, kpub
	return [kpriv, kpub]

# generate a 'random' prime number in the range [min_val, max_val]
# return the prime
def get_prime(min_val, max_val):
	p = randint(min_val, max_val)
	while p%2==0 and not test_prime(p, 4**-5):
		p = randint(min_val, max_val)
	return p