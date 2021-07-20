from heapq import heappush, heappop
INF = 10 ** 9 + 7
 
def Dijkstra(s, f):
	global dist
	pq = [(0, s)]
	dist[s] = 0
     
	while pq:
		w, u = heappop(pq)
		if u == f:
			break
         
		if w > dist[u]:
			continue
         
		for weight, v in graph[u]:
			if w + weight < dist[v]:
				dist[v] = w + weight
				heappush(pq, (dist[v], v))
 
Q = int(input())
 
for t in range(1, Q + 1):
	n, m, S, T = map(int, input().split())
	graph = [[] for _ in range(n)]    
	dist = [INF] * n
     
	for _ in range(m):
		u, v, w = map(int, input().split())
		graph[u].append((w, v))
		graph[v].append((w, u))
 
	Dijkstra(S, T)
     
	print('Case #{}: '.format(t), end='')
	print(dist[T] if dist[T] != INF else "unreachable")
