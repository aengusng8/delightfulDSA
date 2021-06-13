#Solution 1:
n, k = map(int, input().split())
cnt = [0] * 101

for _ in range(n):
    s = input()
    cnt[len(s)] += 1

password = input()
best_time = worst_time = 0

for i in range(len(password)):
    best_time += cnt[i]

worst_time = best_time + cnt[len(password)] - 1

best_time += (best_time // k) * 5
worst_time += (worst_time // k) * 5

print(best_time + 1, worst_time + 1, sep=' ')

#Solution 2:
"""
n,k = map(int, input().split())
list_n = []
list_len = []

for i in range(n):
	list_n.append(input())
	
for x in list_n:
	list_len.append(len(x))
password = input()
list_len.sort()
unique_len = list(set(list_len))

count_1 = 0
count_2 = 0
for i in range(len(unique_len)):
	for j in range(n):
		if unique_len[i] == list_len[j]:
			if unique_len[i] < len(password):
				count_1 += 1
			elif unique_len[i] == len(password):
				count_2 += 1
min = (count_1 + 1)*1 + int(count_1/k)*5
max = (count_1 + count_2) + int((count_1 + count_2 - 1)/k)*5
print(min," ",max)
"""
