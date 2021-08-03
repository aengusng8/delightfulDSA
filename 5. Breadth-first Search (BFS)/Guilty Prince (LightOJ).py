from queue import Queue

MAX = 21
TC = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(r, c):
	return r in range(m) and c in range(n)

class Cell():
	def __init__(self, _r, _c):
		self.r = _r
		self.c = _c

def BFS(start):
	visited = [[False] * MAX for i in range(MAX)]
	global count
	q = Queue()
	q.put(start)
	visited[start.r][start.c] = True

	while not q.empty():
		processing = q.get()

		for i in range(4):
			r = dr[i] + processing.r
			c = dc[i] + processing.c 
			if isValid(r, c) and maze[r][c] == "." and visited[r][c] == False:
				visited[r][c] = True
				q.put(Cell(r, c))
				count += 1

	return count

for k in range(1, TC + 1):
	n, m = map(int, input().split())
	maze = [None] * MAX
	count = 1

	#find @ = start
	for i in range(m):
		maze[i] = input()
		for j in range(n):
			if maze[i][j] == "@":
				start = Cell(i, j)

	print("Case {}: {}".format(k, BFS(start)))
