def DFS(src):
	global node, max_dist
	dist = [-1] * (V + 1)
	s = [src]
	dist[src] = 0

	while len(s):
		u = s.pop()

		for v, w in graph[u]:
			if dist[v] == -1:
				dist[v] = dist[u] + w
				max_dist = max(max_dist, dist[v])
				s.append(v)
    
	node = dist.index(max_dist)

t = int(input())

for _ in range(t):
	V = int(input())
	E = V - 1
	graph = [[] for _ in range(V + 1)]

	for i in range(E):
		u, v, w = map(int, input().split())
		graph[u].append((v, w))
		graph[v].append((u, w))
    
	node = 0
	max_dist = 0

	DFS(1)
	DFS(node)

	print(max_dist)
