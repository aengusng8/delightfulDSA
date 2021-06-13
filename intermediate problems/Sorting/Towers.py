n = int(input())
bars = list(map(int, input().split()))

bars.sort()

count = 1
max_height = 1
for i in range(n-1):
	if bars[i] == bars[i+1]:
		count += 1
	else:
		count = 1
	max_height = max(max_height, count)

print(max_height, len(set(bars)))
