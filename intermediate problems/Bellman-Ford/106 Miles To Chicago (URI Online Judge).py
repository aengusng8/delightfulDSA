#probability

def BellmanFord():
	prob[1] = 1.0

	for i in range(n - 1):
		for edge in graph:
			u, v, w = edge

			if prob[v] != -1:								#!!! For undirected graph only
				prob[u] = max(prob[u], prob[v] * w)		
			if prob[u] != -1:								#!!! For undirected graph only
				prob[v] = max(prob[v], prob[u] * w)				

while True:
	line = list(map(int, input().split()))
	if len(line) == 1:
		break
	
	graph = []
	n, m = line[0], line[1]
	
	for _ in range(m):
		u, v, c = map(int, input().split())
		graph.append((u, v, c / 100))
	
	prob = [-1.0] * (n + 1)
	BellmanFord()

	print("{:.6f} percent".format(prob[n] * 100))
