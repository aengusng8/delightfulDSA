import math

def inp():
	return map(int, input().split(' '))

def f(p , q , r , s , t , u , x):
	return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u


while True:
	try:
		p, q, r, s, t, u = map(float, input().split(' '))

		if f(p, q, r, s, t, u, 1.0) > 1e-9 or p + r + u < 0:
			print("No solution")
			continue

		res = -1
		lo = 0.000
		hi = 1.000
		for i in range(100):
			mid = (lo + hi) / 2.0
			F = f(p, q, r, s, t, u, mid)
			if F > 0:
				lo = mid
			else:
				hi = mid
		print('{:0.4f}'.format(lo))
	except EOFError:
		break
    
"""
# Newton's method
import math

eps = 1e-7

def f(p , q , r , s , t , u , x):
	return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * (x**2) + u

def derivative_f(p , q , r , s , t , u , x)
	return -p * math.exp(-x) + q * math.cos(x) - r * math.sin(x) + s / (math.cos(x) ** 2) + 2 * t * x

while True:
	x = 1
	if f(p , q , r , s , t , u , x)/derivative_f(p , q , r , s , t , u , x) < eps
(...)

"""
