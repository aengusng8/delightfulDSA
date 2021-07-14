import heapq

n = int(input())
top3 = []
rest = []
nReviews = 0

for _ in range(n):
	line = list(map(int, input().split()))

	if line[0] == 1:
		x = line[1]
		nReviews += 1

		if len(top3) != 0 and top3[0] < x:
			heapq.heappush(rest, -heapq.heappop(top3))
			heapq.heappush(top3, x)
		else:
			heapq.heappush(rest, -x)

		if nReviews % 3 == 0:
			heapq.heappush(top3, -heapq.heappop(rest))
	else:
		if len(top3) == 0:
			print("No reviews yet")
		else:
			print(top3[0])
