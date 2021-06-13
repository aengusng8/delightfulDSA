#Solution 1
"""
na, nb = map(int, input().split()) 
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
"""
print('YES' if a[k - 1] < b[nb - m] else 'NO')
#Solution 2

list_1 = list(map(int, input().split()))
N_A = list_1[0]
N_B = list_1[1]

list_2 = list(map(int, input().split()))
K = list_2[0]
M = list_2[1]

A = list(map(int, input().split()))
B = list(map(int, input().split()))
#--
selected_A = []
selected_B = []
for i in range(K):
	selected_A.append(A[i])
B.sort(reverse = True)
for i in range(M):
	selected_B.append(B[i])

if max(selected_A) < min(selected_B):
	print("YES")
else:
	print("NO")






