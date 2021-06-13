N, T = map(int, input().split())
A = list(map(int, input().split()))

max_book = 0
read_time = 0
start_book = 0

for end_book in range(N):
	read_time += A[end_book]
	while read_time > T:
		read_time -= A[start_book]
		start_book += 1
	max_book = max(max_book, end_book - start_book + 1)
	
print(max_book)
