import heapq

class Node:
	def __init__(self, _id, _weight):
		self.id = _id
		self.weight = _weight
	def __lt__(self, other):
		return self.weight < other.weight

def Dijkstra(s, f):
	dist = [10**9] * (N + 5)
	pq = [Node(s, 0)]
	dist[s] = 0

	while len(pq) != 0:
		top = heapq.heappop(pq)
		u = top.id
		w = top.weight

		if u == f:
			break

		if w != dist[u]:
			continue

		for neighbor in graph[u]:
			if dist[neighbor.id] > w + neighbor.weight:
				dist[neighbor.id] = w + neighbor.weight
				heapq.heappush(pq, Node(neighbor.id, dist[neighbor.id]))

	return dist[f]

tc = int(input())

for _ in range(tc):
	N = int(input())
	graph = [[] for i in range(N + 5)]
	cities = [-1] * (N + 5)

	for u in range(1, N + 1):
		name = input()
		cities[u] = name
		neighbors = int(input())

		for i in range(neighbors):
			v, w = map(int, input().split())
			graph[u].append(Node(v, w))

	Q = int(input())

	for i in range(Q):
		sCity, fCity = input().split()
		s = cities.index(sCity)
		f = cities.index(fCity)

		print(Dijkstra(s, f))

	input()
