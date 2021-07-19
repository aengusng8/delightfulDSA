def Try(a_list, mid, n):
	curEnergy = mid 
	for i in range(1, n + 1):
		diff = a_list[i] - a_list[i - 1]

		if curEnergy < diff:
			return False
		elif curEnergy == diff:
			curEnergy -= 1
	return True
 
T = int(input())

for tc in range(1, T + 1):
	print("Case {}: ".format(tc), end = "")

	n = int(input())
	a_list = [0] + list(map(int, input().split()))

	left = 1
	right = ans = a_list[n]

	while left <= right:
		mid = (left + right) // 2

		if Try(a_list, mid, n) == True:
			ans = mid 
			right = mid - 1
		else:
			left = mid + 1

	print(ans)
