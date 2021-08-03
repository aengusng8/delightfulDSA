  n = int(input())
list = list(map(int, input().split()))

sorted_list = sorted(list)

intermittent_list = []
for i in range(n):
	intermittent_list.append(sorted_list[i] == list[i])

if False in intermittent_list:
	first_False = intermittent_list.index(False)
	intermittent_list.reverse()
	last_False = (n - 1) - intermittent_list.index(False)
else: 
	print("yes")
	print(1,1)
	exit()


#print(first_False, last_False) 
i = first_False
j = last_False
while i < j:
	list[i], list[j] = list[j], list[i]
	i += 1
	j -= 1

#print(list)
for i in range(n):
	if list[i] != sorted_list[i]:
		print("no")
		exit()

print("yes")
print(first_False + 1, last_False + 1)  
