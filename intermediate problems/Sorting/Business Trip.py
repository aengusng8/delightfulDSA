k = int(input())
months = list(map(int, input().split()))

months.sort(reverse = True)

sum = 0
i = 0
count = 0

while sum < k and i < 12:
	sum += months[i]
	count += 1
	i += 1
print(count if sum >= k else -1)
