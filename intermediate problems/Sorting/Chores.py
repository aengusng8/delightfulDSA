n, a, b = map(int, input().split())
H = list(map(int, input().split()))

H.sort()

if H[b-1] != H[b]:
	print(H[b] - H[b-1])
else:
	print(0)
