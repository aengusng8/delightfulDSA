def DFS(x):
	s = [x]
	visited[x] = True

	while len(s):
		u = s.pop()

		for v in graph[u]:
			if visited[v] == False:
				visited[v] = True
				s.append(v)

TC = int(input())

for _ in range(TC):
	V = int(input())
	E = int(input())

	graph = [[] for i in range(V)]
	visited = [False] * (V)
	count = 0

	if E == 0:
		print(V)
	else:
		for i in range(E):
			u, v = map(int, input().split())
			graph[u].append(v)
			graph[v].append(u)

		for x in range(V):
			if not visited[x]:
				DFS(x)
				count += 1


		print(count)
