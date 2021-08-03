import heapq

while True:
	N = int(input())
	if not N:
		break

	setNumbers = list(map(int, input().split()))
	result = 0

	heapq.heapify(setNumbers)

	while len(setNumbers) > 1:
		first = heapq.heappop(setNumbers)
		second = heapq.heappop(setNumbers)

		result += (first + second)

		heapq.heappush(setNumbers, first + second)

	print(result)
