import heapq

Q = int(input())
pq = []
pqRemove = []

for i in range(Q):
	line = list(map(int, input().split()))

	if line[0] == 1:
		heapq.heappush(pq, line[1])
	elif line[0] == 2:
		heapq.heappush(pqRemove, line[1])
	else:
		while len(pqRemove) != 0 and pq[0] == pqRemove[0]:
			heapq.heappop(pq)
			heapq.heappop(pqRemove)

		print(pq[0])
