S = str(input())

A = abs(ord("a") - ord(S[0]))
B = abs(26 - A)

rotations = min(A,B)

for i in range(len(S) - 1):
	A = abs(ord(S[i]) - ord(S[i+1]))
	#B = abs((ord("z") - ord("a") + 1) - A)
	B = abs(26 - A)
	rotations += min(A,B)
print(rotations)
