import heapq

class Node:
	def __init__(self, _id, _weight):
		self.id = _id
		self.weight = _weight
	def __lt__(self, other):
		return self.weight < other.weight

def Dijkstra(s, f, timelimit):
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

	return dist[f] <= timelimit

N = int(input())
f = int(input())
timelimit = int(input())

graph = [[] for _ in range(N + 5)]

M = int(input())
for _ in range(M):
	u, v, w = map(int, input().split())
	graph[u].append(Node(v, w))

count = 0
for i in range(1, N + 1):
	if Dijkstra(i, f, timelimit):
		count += 1

print(count)
