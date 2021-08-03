INF = 10 ** 9
MAX = 28

def FloydWarshall(dist):
	for k in range(MAX):
		for i in range(MAX):
			if dist[i][k] == INF:
				continue

			for j in range(MAX):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


while True:
	N = int(input())
	if N == 0:
		break

	distY = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]
	distM = [[0 if i == j else INF for j in range(MAX)] for i in range(MAX)]

	for _ in range(N):
		age, dir, x, y, weight = input().split()
		u, v = map(lambda char: ord(char) - ord("A"), (x, y))
		weight = int(weight) 

		if age == "Y":
			distY[u][v] = min(distY[u][v], weight)
			if dir == "B":
				distY[v][u] = min(distY[v][u], weight)
		else:
			distM[u][v] = min(distM[u][v], weight)
			if dir == "B":
				distM[v][u] = min(distM[v][u], weight)

	me, him = map(lambda char: ord(char) - ord("A"), input().split())
	FloydWarshall(distY)
	FloydWarshall(distM)

	minDist = INF
	result = []

	for i in range(MAX):
		if distY[me][i] != INF and distM[him][i] != INF and minDist >= distY[me][i] + distM[him][i]:
			minDist = distY[me][i] + distM[him][i]
			result.append((minDist, i))

	if not result:
		print("You will never meet.")
	else:
		result.sort()
		print(minDist, end = "")

		for destination in result:
			if destination[0] != minDist:
				break
			print(" " + chr(destination[1] + ord("A")), end = "")

		print()
