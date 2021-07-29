INF = 10 ** 9

def FloydWarshall():
# Với bài này, hai đại lượng là  dist dist và  maxCost maxCost có thể ảnh hưởng qua lại lẫn nhau 
# (dist dist tính theo  maxCost maxCost, còn  maxCost maxCost thì chỉ được cập nhật khi  dist dist thay đổi) 
# nên để đảm bảo rằng cả hai đại lượng đều tối ưu, ta phải duyệt Floyd 2 lần.
	for _ in range(2): 
		for k in range(1, C + 1):
			for i in range(1, C + 1):
				if dist[i][k] == INF:
					continue

				for j in range(1, C + 1):
					if dist[k][j] != INF and dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + max(maxCost[i][k], maxCost[k][j]):
						maxCost[i][j] = max(maxCost[i][k], maxCost[k][j])
						dist[i][j] = dist[i][k] + dist[k][j]


tc = 1
while True:
	C, R, Q = map(int, input().split())

	if (C, R, Q) == (0, 0, 0):
		break

	f = [0] + list(map(int, input().split()))
	maxCost = [[None for i in range(C + 1)] for _ in range(C + 1)]

	for i in range(1, C + 1):
		for j in range(1, C + 1):
			maxCost[i][j] = max(f[i], f[j])

	dist = [[0 if i == j else INF for j in range(C + 1)] for i in range(C + 1)]

	for _ in range(R):
		u, v, w = map(int, input().split())
		dist[u][v] = dist[v][u] = w

	if tc > 1:
		print()

	FloydWarshall()

	print("Case #{}".format(tc))
	tc += 1

	for _ in range(Q):
		u, v = map(int, input().split())
		print(-1 if dist[u][v] == INF else dist[u][v] + maxCost[u][v])
