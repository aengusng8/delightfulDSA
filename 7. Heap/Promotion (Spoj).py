import heapq

selected = [False] * 1000005
maxHeap = []
minHeap = []
totalCost = 0
indexBill = 0

nDays = int(input())

for _ in range(nDays):
	line = list(map(int, input().split()))
    
	for bill in line[1:]:
		indexBill += 1
		heapq.heappush(maxHeap, (-bill, indexBill))
		heapq.heappush(minHeap, (bill, indexBill))

	while selected[maxHeap[0][1]]:
		heapq.heappop(maxHeap)
	while selected[minHeap[0][1]]:
		heapq.heappop(minHeap)

	selected[maxHeap[0][1]] = selected[minHeap[0][1]] = True

	totalCost += (-heapq.heappop(maxHeap)[0] - heapq.heappop(minHeap)[0])

print(totalCost)
