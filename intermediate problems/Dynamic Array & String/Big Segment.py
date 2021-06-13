#Solution 1:
n = int(input())
L, R = [], []
 
for _ in range(n):
    a, b = map(int, input().split())
    L.append(a)
    R.append(b)
 
left, right = min(L), max(R)
 
for i in range(n):
    if left == L[i] and right == R[i]:
        print(i + 1)
        exit()
 
print(-1)
#Solution 2:
"""
n = int(input())

ar = []

for i in range(n):
	a, b = map(int, input().split())
	ar.append( (a, b, i + 1) )

ar.sort() 

min_a = ar[0][0] 
max_b = ar[0][1] 
id = ar[0][2]

for i in range(1, n):
	if (ar[i][0] == min_a):
		if (ar[i][1] > max_b):
			max_b = ar[i][1]
			id = ar[i][2]
	else :
		break

for i in range(n):
	if (ar[i][0] < min_a or ar[i][1] > max_b):
		id = -1

print(id)





"""
