INF = 10**9

class Edge:
	def __init__(self, _source, _target, _weight):
		self.source = _source
		self.target = _target
		self.weight = _weight

def BellmanFord(s):
	dist = [INF] * n
	dist[s] = 0

	for i in range(n - 1):
		for edge in graph:
			u, v, w = edge.source, edge.target, edge.weight
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w

	for edge in graph:
			u, v, w = edge.source, edge.target, edge.weight
			if dist[u] != INF and dist[u] + w < dist[v]:
				return False

	return True

T = int(input())

for _ in range(T):
	n, m = map(int, input().split())
	graph = []

	for i in range(m):
		u, v, w = map(int, input().split())
		graph.append(Edge(u, v, w))

	print("possible" if BellmanFord(0) == False else "not possible")
