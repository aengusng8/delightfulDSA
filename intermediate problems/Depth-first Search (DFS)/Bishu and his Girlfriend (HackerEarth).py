MAX = 1000 + 5
graph = [[] for _ in range(MAX)]
visited = [False] * MAX
dist = [0] * MAX

N = int(input())

for _ in range(N - 1):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

def DFS(s):
	stack = [s]
	visited[s] = True

	while len(stack):
		processing = stack.pop()

		for x in graph[processing]:
			if visited[x] == False:
				visited[x] = True
				dist[x] = dist[processing] + 1
				stack.append(x)

DFS(1)
Q = int(input())

min_dist = MAX
id = 0

for i in range(Q):
	x = int(input())
	if dist[x] < min_dist or (dist[x] == min_dist and id > x):
		min_dist = dist[x]
		id = x 

print(id)
