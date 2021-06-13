N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = 0

while i < len(A):
	if A[i] in B:
		B.remove(A[i])
		A.remove(A[i])
		i -= 1
	i += 1


index_A = len(A) - 1
while index_A >= 0:
	last_index_B = len(B) - 1 
	if A[index_A] < B[last_index_B]:
		A.pop(index_A)
		B.pop(last_index_B)
	index_A -= 1

print(len(A))
