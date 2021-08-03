from queue import Queue

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def BFS(sr, sc, fr, fc):
	q = Queue()
	q.put((sr, sc))
	gameMap[sr][sc] = "X"

	while not q.empty():
		ur, uc = q.get()

		for i in range(4):
			r = dr[i] + ur
			c = dc[i] + uc

			if (r, c) == (fr, fc) and gameMap[r][c] == "X":
				return True

			if r in range(n) and c in range(m) and gameMap[r][c] == ".":
				gameMap[r][c] = "X"
				q.put((r, c))

	return False

n, m = map(int, input().split())
gameMap = [list(input()) for i in range(n)] 

sr, sc = map(int, input().split())
fr, fc = map(int, input().split())

print("YES" if BFS(sr - 1, sc - 1, fr - 1, fc - 1 ) else "NO")
