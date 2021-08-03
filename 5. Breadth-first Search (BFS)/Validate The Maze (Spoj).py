from queue import Queue

MAX = 21

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

maze = [None] * MAX
visited = [[False] * MAX for _ in range(MAX)]

class Cell:
	def __init__(self, _r, _c):
		self.r = _r
		self.c = _c

def isValid(r, c):
	return r in range(m) and c in range(n)

def BFS(start, finish):
	q = Queue()
	q.put(start)
	visited[start.r][start.c] = True

	while not q.empty():
		processing = q.get()

		if processing.r == finish.r and processing.c == finish.c:
			return True

		for i in range(4):
			r = processing.r + dr[i]
			c = processing.c + dc[i]

			if isValid(r, c) and maze[r][c]  == "." and not visited[r][c]:
				q.put(Cell(r,c))
				visited[r][c] = True

	return False


TC = int(input())

for _ in range(TC):
	m, n = map(int, input().split())
	
	entrance = []

	for i in range(m):
		maze[i] = input()

		for j in range(n):
			visited[i][j] = False
			if maze[i][j] == "." and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
				entrance.append(Cell(i, j))

	if (len(entrance)) != 2:
		print("invalid")
	else:
		print("valid" if BFS(entrance[0], entrance[1]) else "invalid") 

