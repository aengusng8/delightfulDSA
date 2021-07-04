import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 5)]
maxCount = 0

def DFS(u):
	visited[u] = True
	count = 1
	
	for x in graph[u]:
		if visited[x] == False:
			count += DFS(x)
			
	return count

for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)

for i in range(1, n + 1):
	visited = [False] * (n + 5)
	maxCount = max(maxCount, DFS(i))
	if maxCount == n:
		print(n)
		exit()

print(maxCount)
