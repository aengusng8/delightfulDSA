n, x = map(int,input().split())
list = list(map(int,input().split()))

list.sort()
sum = 0
for i in range(n):
	sum += list[i] * x
	if x > 1:
		x -= 1

print(sum)
