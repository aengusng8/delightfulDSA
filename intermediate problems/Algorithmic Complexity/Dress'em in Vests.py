N, M, X, Y = map(int, input().split())
A = list(map(int, input().split())) #N: desired sizes of vests
B = list(map(int, input().split())) #M: sizes of the available vests

j = 0
i = 0
output = []
while i < M and j < N:
		if B[i] + X >= A[j] >= B[i] - Y:
			output.append((j +1, i+1))
			j+=1
			i+=1
		elif A[j] >= B[i] - Y:
			i+=1
		elif A[j] <= B[i] + X:
			j+=1
      
print(len(output))
for x in output:
	print(x[0], ' ', x[1])
  

			
