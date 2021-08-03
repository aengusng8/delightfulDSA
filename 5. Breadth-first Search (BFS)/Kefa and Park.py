from queue import Queue

MAX = 10**5 + 5
cat = [0] * MAX
graph = [[] for i in range(MAX)]
visited = [False] * MAX

def BFS(s):
	restaurants = 0
	q = Queue()
	q.put(s)
	visited[s] = True

	cat[s] = (1 if a[s] == 1 else 0)

	while not q.empty():
		processing = q.get()

		for x in graph[processing]:
			if visited[x] == False:
				visited[x] = True

				if a[x] == 1:
					cat[x] = cat[processing] + 1 
				
				if cat[x] <= m:
					if len(graph[x]) == 1:
						restaurants += 1
					else:
						q.put(x)
	
	return restaurants

n, m = map(int, input().split())
a = [None] + list(map(int, input().split()))

for i in range(1, n):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

print(BFS(1))
