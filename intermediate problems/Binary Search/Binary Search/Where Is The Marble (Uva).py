def bsFirst(inputList, left, right, x):
	if left <= right:
		mid = (left + right) // 2

		if (left == mid or inputList[mid - 1] < x) and inputList[mid] == x:
			return mid
		elif x > inputList[mid]:
			return bsFirst(inputList, mid + 1, right, x)
		else:
			return bsFirst(inputList, left, mid - 1, x)
	return -1
	
tc = 0

while True:
	tc += 1
	n, q = map(int, input().split())
	if (n, q) == (0, 0):
		break

	inputList = [int(input()) for _ in range(n)]
	inputList.sort()

	print("CASE# {}:".format(tc))

	for i in range(q):
		x = int(input())

		ans = bsFirst(inputList, 0, n - 1, x)

		print("{} not found".format(x) if ans == -1 else "{} found at {}".format(x, ans + 1))
