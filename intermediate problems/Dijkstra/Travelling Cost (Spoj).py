import heapq
MAX = 505
INF = int(1e9) + 7
graph = [[] for _ in range(MAX)]
dist = [INF] * MAX

class Node:
	def __init__(self, _id, _weight):
		self.id = _id
		self.weight = _weight

	def __lt__(self, other):
		return self.weight < other.weight

def Dijkstra(s):
	pq = [Node(s, 0)]
	dist[s] = 0

	while len(pq) != 0:
		top = heapq.heappop(pq)
		u = top.id
		w = top.weight

		if w != dist[u]:
			continue

		for neighbor in graph[u]:
			if dist[neighbor.id] > w + neighbor.weight:
				dist[neighbor.id] = w + neighbor.weight
				heapq.heappush(pq, Node(neighbor.id, dist[neighbor.id]))

N = int(input())
for _ in range(N):
	A, B, W = map(int, input().split())
	graph[A].append(Node(B, W))
	graph[B].append(Node(A, W))

s = int(input())
Dijkstra(s)

Q = int(input())
for _ in range(Q):
	V = int(input())
	print(dist[V] if dist[V] != INF else "NO PATH")
