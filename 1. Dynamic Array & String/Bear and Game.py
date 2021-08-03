n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

answer = 0

for i in range(len(a) - 1):
	if (a[i+1] - a[i]) <= 15:
		answer = a[i+1] + 15
	else:
		answer = a[i] + 15
		break
if answer > 90:
  print("90")
else: 
  print(answer)
