INF = 10 ** 9

def BellmanFord(s):
	dist[s] = 0

	for i in range(n - 1):
		for j in range(m):
			u, v, w = graph[j]
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w
	
	for i in range(n):
		for j in range(m):
			u, v, w = graph[j]
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = -INF

while True:
	n, m, q, s = map(int, input().split())
	
	if (n, m, q, s) == (0, 0, 0, 0):
		break
	graph = []
	
	for i in range(m):
		u, v, w = map(int, input().split())
		graph.append((u, v, w))
	
	dist = [INF] * n
	BellmanFord(s)

	for _ in range(q):
		f = int(input())
	
		if dist[f] == INF:
			print("Impossible")
		elif dist[f] == -INF:
			print("-Infinity")
		else:
			print(dist[f])
	print()
