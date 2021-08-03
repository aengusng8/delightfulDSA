from queue import Queue

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 250 + 5
backyard = [None] * MAX
nsheep = nwolves = 0

def BFS(sr, sc):
	global nwolves, nsheep
	q = Queue()
	q.put((sr, sc))

	sheep = (1 if backyard[sr][sc] == "k" else 0)
	wolf = (1 if backyard[sr][sc] == "v" else 0)

	backyard[sr][sc] = "#"

	canEscape = False

	while not q.empty():
		ur, uc = q.get()

		for i in range(4):
			r = dr[i] + ur
			c = dc[i] + uc

			if not (r in range(N) and c in range(M)):
				canEscape = True
				continue

			if backyard[r][c] != "#":
				sheep += (1 if backyard[r][c] == "k" else 0)
				wolf += (1 if backyard[r][c] == "v" else 0)
				backyard[r][c] = "#"
				q.put((r,c))

	if canEscape:
		nsheep += sheep
		nwolves += wolf
	else:
		if sheep > wolf:
			nsheep += sheep
		else: 
			nwolves += wolf


N, M = map(int, input().split())

for i in range(N):
	backyard[i] = list(input())

for i in range(N):
	for j in range(M):
		if backyard[i][j] != "#":
			BFS(i, j)

print(nsheep, nwolves, sep = " ")
