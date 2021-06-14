n = int(input())
list = list(map(int, input().split()))

fre = [0] * (10**5 + 5)
j = 0
unique = 0
longest_range = 0
for i in range(n):
	if fre[list[i]] == 0:
		unique += 1
		
	fre[list[i]] += 1

	while unique > 2 and j < n:
		if fre[list[j]] == 1:
			unique -= 1
		fre[list[j]] -= 1
		j += 1

	longest_range = max(longest_range, i - j + 1)

print(longest_range)
