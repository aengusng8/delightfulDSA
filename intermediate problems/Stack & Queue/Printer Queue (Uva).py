# I do not use queue for this problem
TC = int(input())

for _ in range(TC):
	n, index = map(int, input().split())
	if n == 1:
		notCare = input()
		print(1)
		continue

	queue = list(map(int, input().split()))
	time = 0

	while True:
		if index == 0 and queue[0] >= max(queue): 
			time += 1
			print(time)
			break
		else:
			if index == 0:
				queue.append(queue.pop(0))
				index = len(queue) - 1
			elif queue[0] < max(queue):
				queue.append(queue.pop(0))
				index -= 1
			elif queue[0] >= max(queue):
				queue.pop(0)
				index -= 1
				time += 1
