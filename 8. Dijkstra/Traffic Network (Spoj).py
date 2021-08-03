import heapq

def Dijkstra(start, graph, dist):
	pq = [(0, start)]
	dist[start] = 0

	while len(pq) != 0:
		w, u = heapq.heappop(pq)

		if w > dist[u]:
			continue

		for weight, v in graph[u]:
			if dist[v] > w + weight:
				dist[v] = w + weight
				heapq.heappush(pq, (dist[v], v))

T = int(input())
 
for _ in range(T):
	N, M, K, start, finish = map(int, input().split())

	graph_S_all = [[] for _ in range(N + 5)]
	graph_all_T = [[] for _ in range(N + 5)]
	dist_S_all = [10**9] * (N + 5)
	dist_all_T = [10**9] * (N + 5)

	for i in range(M):
		u, v, w = map(int, input().split())
		graph_S_all[u].append((w, v))
		graph_all_T[v].append((w, u))

	Dijkstra(start, graph_S_all, dist_S_all)
	Dijkstra(finish, graph_all_T, dist_all_T)
	result = dist_S_all[finish]

	for i in range(K):
		u, v, w = map(int, input().split())
		result = min(result, dist_S_all[u] + w + dist_all_T[v], dist_S_all[v] + w + dist_all_T[u])

	print(result if result != 10**9 else -1)
