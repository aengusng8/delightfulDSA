def lower_bound(chimps, left, right, x):
	pos = -1

	while left <= right:
		mid = (left + right) // 2

		if chimps[mid] < x:
			pos = max(pos, mid)
			left = mid + 1
		else:
			right = mid - 1

	return "X" if pos == -1 else str(chimps[pos])

def upper_bound(chimps, left, right, x):
	pos = a = right + 1

	while left <= right:
		mid = (left + right) // 2

		if chimps[mid] > x:
			pos = min(pos, mid)
			right = mid - 1
		else:
			left = mid + 1

	return "X" if pos == a else str(chimps[pos])


N = int(input())
chimps = list(map(int, input().split()))
Q = int(input())
query = list(map(int, input().split()))

for i in range(Q):
	print(lower_bound(chimps, 0, N - 1, query[i]), upper_bound(chimps, 0, N - 1, query[i]))
