def FloydWarshall():
	for k in range(V):
		for i in range(V):
			if dist[i][k] == 0:
				continue
			for j in range(V):
				dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

tc = 1
while True:
	V = int(input())
	if V == 0:
		break

	dist = [[1 if i == j else 0 for j in range(V)] for i in range(V)]
	currencies = [input().strip() for _ in range(V)]

	E = int(input())
	for _ in range(E):
		source_Currency, rate, destination_Currency = input().split()
		u, v = map(lambda x: currencies.index(x), (source_Currency, destination_Currency))
		dist[u][v] = float(rate)

	input()

	FloydWarshall()

	arbitrage = False
	for i in range(V):
		if dist[i][i] > 1:
			arbitrage = True
			break

	print("Case {}: {}".format(tc, "Yes" if arbitrage else "No"))
	tc += 1	
