import heapq

def Dijkstra(start):
	dist = [10**9] * (N + 5)
	
	pq = [(0, start)]
	dist[start] = 0

	while len(pq) != 0:
		w, u = heapq.heappop(pq)

		if dist[u] < w:
			continue

		for weight, v in graph[u]:
			if dist[v] > w + weight:
				dist[v] = w + weight
				heapq.heappush(pq, (dist[v], v))

	return dist


tc = int(input())

for case in range(1, tc + 1):
	N = int(input())
	R = int(input())
	graph = [[] for i in range(N + 5)]

	for i in range(R):
		u, v = map(int, input().split())
		graph[u].append((1, v))
		graph[v].append((1, u))

	S, D = map(int, input().split())

	distS = Dijkstra(S)
	distD = Dijkstra(D)

	res = 0
	for i in range(N):	
		res = max(res, distS[i] + distD[i])

	print("Case {}: {}".format(case, res))
