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
		
"""
def BS_search(a, l, r, value):
    ans = -1
    while l <= r:
        mid = int( (l + r) / 2 )
        if a[mid] == value:
            ans = mid
            r = mid - 1
        elif a[mid] > value:
            r = mid - 1
        else:
            l = mid + 1
    return ans
"""
