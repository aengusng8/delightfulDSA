n = int(input())
a = list(map(int, input().split()))

count = 0

if n == 1:
	if a[0] == 1:
		print("YES")
	else:
		print("NO")
else:
	for x in a:
		if x == 0:
			count += 1
	if count == 1:
		print("YES")
	else:
		print("NO")
