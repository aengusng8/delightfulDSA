INF = (1 << 30) * 100 + 7

def BellmanFord(s):
	dist = [INF] * n
	dist[s] = 0

	for i in range(n - 1):
		for edge in graph:
			u, v, w = edge
			if dist[u] != INF and dist[v] > dist[u] + w:
				dist[v] = dist[u] + w 

	for i in range(n - 1):
		for edge in graph:
			u, v, w = edge
			if dist[u] != INF and dist[v] > dist[u] + w:
				dist[v] = -INF

	return dist

tc = 1
while True:
	n = int(input())
	if n == 0:
		break

	monuments = []
	graph = []
	n_dist = [[] for _ in range(n)]

	for u in range(n):
		name, *weights = input().split()
		monuments.append(name)

		for v in range(n):
			w = int(weights[v])
			
			if u != v and w == 0:
				continue
			if u == v and w > 0:
				w = 0

			graph.append((u, v, w))

	for i in range(n):
		n_dist[i] = BellmanFord(i)

	print("Case #{}:".format(tc))
	tc += 1

	q = int(input())

	for i in range(q):
		u, v = map(int, input().split())
		if n_dist[u][v] <= -INF: 		#BE CAREFUL HERE!
			print("NEGATIVE CYCLE")
		else:
			print("{}-{} {}".format(monuments[u], monuments[v], n_dist[u][v] if n_dist[u][v] != INF else "NOT REACHABLE"))
