INF = 10 ** 9

def BellmanFord(s):
	dist = [INF] * (n + 1)
	dist[s] = 0

	for i in range(n):
		for edge in graph:
			u, v, w = edge
	        
			if dist[u] != INF and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w
	            
				if i == n - 1:                  #!!!
					return True											
    
	return False

T = int(input())

for _ in range(T):
	n, m = map(int, input().split())
	graph = []

	for i in range(m):
		u, v, w = map(int, input().split())
		graph.append((u, v, -w))

	print("Yes" if BellmanFord(1) else "No")
