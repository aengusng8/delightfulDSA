n = int(input())
cards = list(map(int, input().split()))

player = 1
points = [0, 0]
i = 0
j = n - 1

while i <= j:
	if cards[i] <= cards[j]:
		points[player] += cards[j]
		j -= 1
	else:
		points[player] += cards[i]
		i += 1
	player = 1 - player

print(points[0], points[1])