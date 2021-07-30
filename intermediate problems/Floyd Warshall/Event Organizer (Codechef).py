MAX = 48

def FloydWarshall():
	for k in range(MAX + 1):
		for i in range(MAX + 1):
			for j in range(MAX + 1):
				if i <= k <= j:					# !!!
					dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())
for _ in range(T):
	N = int(input())
	dist = [[0] * (MAX + 1) for i in range(MAX + 1)]
	
	for i in range(N):
		S, E, C = map(int, input().split())
		dist[S][E] = max(C, dist[S][E])
	
	FloydWarshall()
	print(dist[0][MAX])
