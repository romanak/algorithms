def karatsuba(x, y):
	"""Assumes x, y are positive integers.
		Returns the product x*y"""

	x = int(x)
	y = int(y)

	nx = 1
	while (x/10**nx > 1):
		nx += 1

	ny = 1
	while (y/10**ny > 1):
		ny += 1

	n = max(nx, ny)

	if n == 1:
		return x*y

	i = 2
	while (n/i > 1):
		i *= 2

	xk = i - nx
	yk = i - ny

	x *= 10**xk
	y *= 10**yk

	a = x//(10**(i//2))
	b = x - a*(10**(i//2))
	c = y//(10**(i//2))
	d = y - c*(10**(i//2))
	p = a + b
	q = c + d

	ac = karatsuba(a, c)
	bd = karatsuba(b, d)
	pq = karatsuba(p, q)
	adbc = pq - ac - bd

	return (ac*10**i + adbc*10**(i//2) + bd)//(10**(xk+yk))

a = karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
b = 3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627

if a == b:
    print(a)