INF = 10 ** 9

def FloydWarshall():
	for k in range(M):
		for i in range(M):
			if dist[i][k] == INF:
				continue

			for j in range(M):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())

for _ in range(T):
	firstLine = input()
	M = len(firstLine)
	dist = [[INF] * M for i in range(M)]
	graph = []

	for i in range(M):
		if i == 0:
			graph.append(firstLine)
		else:
			graph.append(input())

		for j in range(M):
			if graph[i][j] == "Y":
				dist[i][j] = 1
			elif i == j:
				dist[i][j] = 0

	FloydWarshall()
	ID, nFriends = 0, 0

	for i in range(M):
		count = 0

		for j in range(M):
			if dist[i][j] == 2:
				count += 1

			if count > nFriends:
				nFriends = count
				ID = i

	print(ID, nFriends)
