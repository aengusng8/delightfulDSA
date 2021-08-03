from queue import Queue

def BFS(s):
	q = Queue()
	q.put(s)
	visited[s] = True

	while not q.empty():
		u = q.get()

		for v in adjacent_graph[u]:
			if not visited[v]:
				visited[v] = True
				dist[v] = dist[u] + 1
				q.put(v)

TC = int(input())
MAX = 1000 + 5

for _ in range(TC):
	vertices, edges = map(int, input().split())

	adjacent_graph = [[] for i in range(MAX)]
	visited = [False] * MAX
	dist = [0] * MAX

	for i in range(edges):
		u, v = map(int, input().split())
		adjacent_graph[u].append(v)
		adjacent_graph[v].append(u)

	s = int(input())

	BFS(s)

	for i in range(1, vertices + 1):
		if i == s:
			continue
		print(dist[i] * 6 if visited[i] else -1, end = " ")

	print()
