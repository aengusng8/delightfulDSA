import heapq
INF = 10**9
MAX = 505

def Dijkstra(start, graph):
	dist = [INF] * MAX

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


while True:
	N, M = map(int, input().split())
	if (N, M) == (0, 0):
		break

	S, D = map(int, input().split())
	graphS = [[] for _ in range(N + 5)]
	graphD = [[] for _ in range(N + 5)]
	graph_withoutShortest = [[] for _ in range(N + 5)]

	for i in range(M):
		u, v, w = map(int, input().split())
		graphS[u].append((w, v))
		graphD[v].append((w, u))

	distS = Dijkstra(S, graphS)
	distD = Dijkstra(D, graphD)

	shortestDist = distS[D]

	for u in range(N):
		for w, v in graphS[u]:
			if distS[u] + w + distD[v] != shortestDist:
				graph_withoutShortest[u].append((w, v))

	dist_Ans = Dijkstra(S, graph_withoutShortest)

	print(dist_Ans[D] if dist_Ans[D] != INF else -1)
