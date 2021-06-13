n = int(input())
rating = list(map(int, input().split()))

rank = [0] * 2001
sorted_set = sorted(list(set(rating)), reverse = True)

#print(sorted_set)
start_rank = 1
rank[sorted_set[0]] = start_rank

for i in range(1, len(sorted_set)):
	start_rank = start_rank + rating.count(sorted_set[i-1])
	rank[sorted_set[i]] = start_rank 

for i in range(n):
	print(rank[rating[i]], end =" ") 
