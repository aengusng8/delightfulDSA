def binary_search(money, left, right, comp):
	while left <= right:
		mid = (left + right) // 2

		if money[mid] == comp:
			return True
		elif money[mid] > comp:
			right = mid - 1
		else:
			left = mid + 1

	return False

tc = int(input())

for _ in range(tc):
	n, m = map(int, input().split())
	money = list(map(int, input().split()))

	money.sort()

	nPairs = 0

	for i in range(n):
		comp = m - money[i]
		if binary_search(money, i + 1, n - 1, comp):
			nPairs += 1

	print(nPairs)
