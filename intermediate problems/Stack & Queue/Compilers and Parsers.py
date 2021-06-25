TC = int(input())
 
for _ in range(TC):
	s = input()
	expr = []
	ans = 0
 
	for i in range(len(s)):
		if s[i] == '<':
			expr.append(s[i])
		elif len(expr) == 0:
			break
		else:
			expr.pop()
			ans = i + 1 if len(expr) == 0 else ans

	print(ans)
