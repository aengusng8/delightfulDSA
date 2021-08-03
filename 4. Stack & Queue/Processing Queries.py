#Solution 1:
from queue import Queue

N, B = map(int, input().split())
q = Queue()
processing = 0

for _ in range(N):
	t, d = map(int, input().split())

	while q.qsize() != 0 and t >= q.queue[0]:
		q.get()

	if q.qsize() <= B:
		processing = max(t, processing) + d
		q.put(processing)
		print(processing, end = " ")
	else:
		print(-1, end = " ")
