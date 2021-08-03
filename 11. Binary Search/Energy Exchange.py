# m * n < sumEnergy - sumLoss

n, k = map(int, input().split())
a = list(map(int, input().split()))

sumEnergy = sum(a)

right = 1000
left = 0

while right - left > 1e-7:
	mid = (right + left) / 2

	sumTranfer = 0

	for x in a:
		if x > mid:
			sumTranfer += (x - mid)

	sumLoss = sumTranfer * k / 100

	if mid * n < sumEnergy - sumLoss:
		left = mid 
	else:
		right = mid 

print("%.9f" %left)
