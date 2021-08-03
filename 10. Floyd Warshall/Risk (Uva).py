INF = 10 ** 9
N = 20

def FloydWarshall():
	for k in range(1, N + 1):
		for i in range(1, N + 1):
			if dist[i][k] == INF: 
				continue

			for j in range(1, N + 1):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

t = 1
while True:
	try:
		dist = [[INF if i != j else 0 for j in range(N + 1)] for i in range(N + 1)]
		for i in range(1, N):
			for j in list(map(int, input().split()))[1:]:       # !!!
				dist[i][j] = dist[j][i] = 1
		
		FloydWarshall()
		
		print("Test Set #{}".format(t))
		t += 1

		Q = int(input())
		for _ in range(Q):
			u, v = map(int, input().split())
			print('{:2d} to {:2d}: {}'.format(u, v, dist[u][v]))
		print()

	except EOFError:
		break
