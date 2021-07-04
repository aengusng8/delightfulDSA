import sys
sys.setrecursionlimit(10**6)

expression = "ALLIZZWELL"
DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def isValid(r, c):
	return r in range(H) and c in range(W)

def DFS(sr, sc, count):
	global found

	if count == len(expression):
		found = True
		return

	for dr, dc in DIR:
		r = dr + sr
		c = dc + sc

		if isValid(r, c) and grid[r][c] == expression[count] and visited[r][c] == False:
			visited[r][c] = True
			DFS(r, c, count + 1)
			visited[r][c] = False

TC = int(input())

for _ in range(TC):
	H, W = map(int, input().split())
	visited = [[False] * W for i in range(H)]
	grid = [[] for i in range(H)]

	found = False

	for i in range(H):
		grid[i] = list(input())

	for i in range(H):
		for j in range(W):
			if grid[i][j] == expression[0] and not found:
				DFS(i, j, 1)

	print("YES" if found else "NO")
	input()
