from queue import Queue

class Car:
	def __init__(self, _id, _arriveTime):
		self.id = _id
		self.arriveTime = _arriveTime

TC = int(input())

for _ in range(TC):
	N, T, M = map(int, input().split())
	qBank = [[], []]
	qBank[0] = Queue()
	qBank[1] = Queue()
	answer = [0] * (M + 5)

	for i in range(M):
		arriveTime, Bank = input().split()

		if Bank == "left":
			qBank[0].put(Car(i, int(arriveTime)))
		else:
			qBank[1].put(Car(i, int(arriveTime)))

	curTime, curBank = 0, 0
	waiting = (not qBank[0].empty()) + (not qBank[1].empty())
	### finish initializing!
	while waiting:
		if waiting == 1:
			nextTime = qBank[0].queue[0].arriveTime if qBank[1].empty() else qBank[1].queue[0].arriveTime
		else:
			nextTime = min(qBank[0].queue[0].arriveTime, qBank[1].queue[0].arriveTime)

		curTime = max(curTime, nextTime)
		carried = 0

		while not qBank[curBank].empty():
			car = qBank[curBank].queue[0]
			if car.arriveTime <= curTime and carried < N:
				carried += 1
				answer[car.id] = curTime + T
				qBank[curBank].get()
			else:
				break

		curBank = 1 - curBank
		curTime += T
		waiting = (not qBank[0].empty()) + (not qBank[1].empty())

	for i in range(M):
		print(answer[i])

	if _ < TC - 1:
		print()
