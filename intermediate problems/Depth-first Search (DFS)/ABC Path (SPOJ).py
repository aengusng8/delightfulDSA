TC = 0

DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def isValid(r, c):
	return r in range(H) and c in range(W)

def DFS(sr, sc):
	s = [(sr, sc)]
	answer = 1

	while len(s):
		ur, uc = s.pop()

		for dr, dc in DIR:
			r = dr + ur
			c = dc + uc

			if isValid(r, c) and ord(grid[r][c]) == ord(grid[ur][uc]) + 1 and visited[r][c] == False:
				visited[r][c] = True
				s.append((r, c))
				dist[r][c] = dist[ur][uc] + 1

				answer = max(answer, dist[r][c])
	return answer


while True:
	TC += 1
	H, W = map(int, input().split())

	if (H, W) == (0, 0):
		break

	visited = [[False] * W for i in range(H)]
	dist = [[1] * W for i in range(H)]
	grid = [[] for i in range(H)]
	answer = 0

	for i in range(H):
		grid[i] = list(input())

	for i in range(H):
		for j in range(W):
			if grid[i][j] == "A":
				answer = max(answer, DFS(i, j))

	print("Case {}: {}".format(TC, answer))
