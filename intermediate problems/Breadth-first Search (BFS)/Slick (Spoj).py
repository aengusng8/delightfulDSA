from queue import Queue

MAX = 250 + 5

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(r, c):
	return r in range(m) and c in range(n)

class Cell:
	def __init__(self, _r, _c):
		self.r = _r
		self.c = _c

def DFS(start):
	q = Queue()
	q.put(start)
	visited[start.r][start.c] = True
	global answer
	size = 1

	while not q.empty():
		processing = q.get()
		for i in range(4):
			r = dr[i] + processing.r
			c = dc[i] + processing.c

			if isValid(r, c) and maze[r][c] == 1 and visited[r][c] == False:
				size += 1
				q.put(Cell(r, c))
				visited[r][c] = True
	answer[size] += 1

while 0<1:
	m, n = map(int, input().split())
	if (m, n) == (0, 0):
		break

	count = 0
	maze = [list(map(int, input().split())) for i in range(m)]
	visited = [[False] * MAX for i in range(MAX)]
	answer = [0] * (m * n + 5)

	for i in range(m):
		for j in range(n):
			if visited[i][j] == False and maze[i][j] == 1:
				DFS(Cell(i, j))
				count += 1


	print(count)
	for i in range(len(answer)):
		if answer[i] != 0:
			print(i, answer[i], sep = " ")
