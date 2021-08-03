def binary_search(inputList, left, right, comp):
	while left <= right:
		mid = (left + right) // 2

		if inputList[mid] == comp:
			return True
		elif inputList[mid] > comp:
			right = mid - 1
		else:
			left = mid + 1

	return False

N, K = map(int, input().split())
inputList = list(map(int, input().split()))
count = 0

inputList.sort()

for i in range(N):
	comp = inputList[i] + K
	if binary_search(inputList, i + 1, N - 1, comp):
		count += 1

print(count)
