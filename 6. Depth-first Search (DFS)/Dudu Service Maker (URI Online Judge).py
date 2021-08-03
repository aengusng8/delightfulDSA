import sys
sys.setrecursionlimit(10**6)

def DFS(u):
	global found

	visisted[u] = True
	checkedLoop[u] = True
	
	for x in graph[u]:
		if checkedLoop[x] == True:
			found = True
			return
		if visisted[x] == False:
			DFS(x)
	checkedLoop[u] = False

TC = int(input())

for _ in range(TC):
	found = False
	N, M = map(int, input().split())
	graph = [[] for i in range(N + 5)]
	visisted = [False] * (N + 5) 
	checkedLoop = [False] * (N + 5)

	for i in range(M):
		u, v = map(int, input().split())
		graph[u].append(v)

	for i in range(N):
		if visisted[i] == False:
			DFS(i)

	print("YES" if found else "NO")
