import heapq

class PQEntry:
	def __init__(self, value):
		self.value = value
	def __lt__(self, other):
		return self.value > other.value

N = int(input())
input_list = list(map(int, input().split()))
h = []

for i in range(N):
	heapq.heappush(h, PQEntry(input_list[i]))

	if len(h) < 3: 
		print(-1)
	else:
		first = heapq.heappop(h).value
		second = heapq.heappop(h).value
		third = heapq.heappop(h).value

		print(first * second * third)

		heapq.heappush(h, PQEntry(first))
		heapq.heappush(h, PQEntry(second))
		heapq.heappush(h, PQEntry(third))
