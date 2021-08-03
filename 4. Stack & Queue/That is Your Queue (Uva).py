from queue import Queue
test_case = 1

while 0 < 1:
	P, C = map(int, input().split())

	if (P,C) == (0,0):
		break

	q = Queue()
	for i in range(1, min(P, C) + 1):
		q.put(i)

	print("Case {}:".format(test_case))
	test_case += 1

	for i in range(C):
		line = input().split()

		if line[0] == "N":
			print(q.queue[0])
			q.put(q.get())
		else:
			x = int(line[1])
			q.put(x)

			for i in range(q.qsize() - 1):
				if q.queue[0] != x:
					q.put(q.get())
				else:
					q.get()
