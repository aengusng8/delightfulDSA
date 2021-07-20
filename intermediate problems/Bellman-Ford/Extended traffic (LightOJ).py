INF = 10**9

class Edge:
	def __init__(self, _source, _target, _weight):
		self.source = _source
		self.target = _target
		self.weight = _weight

def BellmanFord(s):
	dist = [INF] * (n + 5)
	dist[s] = 0

	for i in range(n - 1):
		for edge in graph:
			u, v, w = edge.source, edge.target, edge.weight
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w

	for i in range(n):
		for edge in graph:
			u, v, w = edge.source, edge.target, edge.weight
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = -INF

	return dist

T = int(input())

for t in range(1, T + 1):
	input()
	n = int(input())
	weight = [0] + list(map(int, input().split()))
	m = int(input())

	graph = []

	for _ in range(m):
		u, v = map(int, input().split())
		graph.append(Edge(u, v, (weight[v] - weight[u]) ** 3))
    
	dist = BellmanFord(1)
	q = int(input())
	print("Case {}:".format(t))

	for _ in range(q):
		f = int(input())
		print(dist[f] if dist[f] != INF and dist[f] >= 3 else "?")
