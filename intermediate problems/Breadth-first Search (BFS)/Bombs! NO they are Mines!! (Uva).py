from queue import Queue

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def isValid(r, c):
	return r in range(R) and c in range(C)


def BFS(sr, sc, fr, fc):
	q = Queue()
	q.put((sr, sc))
	visited[sr][sc] == True

	time = 0

	while not q.empty():
		ur, uc = q.get()

		for i in range(4):
			r = dr[i] + ur
			c = dc[i] + uc

			if isValid(r, c) and maze[r][c] == 0 and visited[r][c] == False:
				dist[r][c] = dist[ur][uc] + 1
				
				if (r, c) == (fr, fc):
					return dist[r][c]
					break
				else:
					visited[r][c] = True
					q.put((r, c))


while True:
	R, C = map(int, input().split())
	if (R, C) == (0, 0):
		exit()

	maze = [[0] * C for _ in range(R)]
	visited = [[False] * C for _ in range(R)]
	dist = [[0] * C for _ in range(R)]

	bomedRow = int(input())

	for _ in range(bomedRow):
		indexList = list(map(int, input().split()))
		row = indexList.pop(0)
		nBom = indexList.pop(0)

		for i in range(nBom):
			maze[row][indexList[i]] = 1

	sr, sc = map(int, input().split())
	fr, fc = map(int, input().split())

	print(BFS(sr, sc, fr, fc))
