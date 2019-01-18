from fractions import Fraction
from random import randint, choice

# val is the secret (the value when x = 0).
# n is the number of points to distribute.
# k is the number of points needed to reconstruct the polynomial.
# Return a list of n random points such that x != 0 for every point.
def split(val, n, k):
	r = 1000
	neg = [1, -1]
	coefs = [choice(neg) * Fraction(randint(1, r), randint(1, r)) for i in range(0, k)]
	coefs.insert(0, val)

	xs = []
	ys = []
	for i in range(n):
		p = 0
		while p == 0 or p in xs:
			p = randint(-r, r)

		xs.append(p)
		ys.append(polyVal(coefs, p))
	
	keys = [(xs[i], ys[i]) for i in range(len(xs))]
	return keys

#given list of coefficents for p, find p(x)
def polyVal(coefs, x):
	val = 0
	i = 0
	for c in coefs:
		val += c * (x**i)
		i += 1
	return val

# points is a list of shares.
# x is the x-coordinate in which to compute the secret at.
# Return the computed secret value.
def interpolate(points, x): #using lagrange interpolation from wiki
	val = 0
	for j in range(len(points)):
		y = points[j][1]
		l = basis(points, x, j)
		val += y*l
	return val

def basis(points, x, j):
	val = 1
	for m in range(len(points)):
		if not m == j:
			a = (x - points[m][0]) 
			b = (points[j][0] - points[m][0])
			v=Fraction(a)/Fraction(b)
			val *= v
	return val

if __name__ == "__main__":
	pass