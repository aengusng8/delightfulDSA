import heapq
INF = 10 ** 9

def Dijkstra(start):
	dist = [INF] * (N + 5)
	
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

N, M, k, x = map(int, input().split())
cities = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	u, v, d = map(int, input().split())
	graph[u].append((d, v))
	graph[v].append((d, u))

A, B = map(int, input().split())

distA = Dijkstra(A)
distB = Dijkstra(B)
res = INF

for city in cities:
	if distB[city] <= x:
		res = min(res, distA[city] + distB[city])
	
print(res if res < INF else -1)
