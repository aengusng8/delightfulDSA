from queue import Queue

MAX = 100000 + 5
MOD = 100000

start, finish = map(int, input().split())
N = int(input())
list = list(map(int, input().split()))

def BFS(start, finish):
	dist = [-1] * MAX
	q = Queue()
	q.put(start)
	dist[start] = 0

	while not q.empty():
		processing = q.get()

		for x in list:
			u = (x * processing) % MOD
			if dist[u] == -1:
				q.put(u)
				dist[u] = dist[processing] + 1
			if u == finish:
				return dist[u]
	return -1

print(BFS(start, finish))
