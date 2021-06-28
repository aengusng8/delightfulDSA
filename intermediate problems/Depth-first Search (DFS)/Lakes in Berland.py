dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
Map = [list(input()) for i in range(n)] 
lakes = [[] for i in range (m*n)]
visited = [[False] * 51 for _ in range(51)]

def DFS(sr, sc):
	s = [(sr, sc)]
	visited[sr][sc] = True

	global lakes

	isOcean = False
	lake = []

	while len(s):
		ur, uc = s.pop()
		lake.append((ur, uc))

		if ur == 0 or ur == n - 1 or uc == 0 or uc == m - 1:
			isOcean = True

		for i in range(4):
			r = dr[i] + ur
			c = dc[i] + uc

			if r in range(n) and c in range(m) and Map[r][c] == "." and not visited[r][c]:
				visited[r][c] = True
				s.append((r, c))


	if not isOcean:
		lakes.append(lake)


for i in range(n):
	for j in range(m):
		if not visited[i][j] and Map[i][j] == '.':
			DFS(i, j)

lakes.sort(key = lambda lake: len(lake))
sumCell = 0

for i in range(len(lakes) - k):
	sumCell += len(lakes[i])
	for r, c in lakes[i]:
		Map[r][c] = '*'

print(sumCell)

for i in range(n):
	print(''.join(Map[i]))
