while 0 < 1:
	n = int(input())
	if n == 0:
		break
	trucks = list(map(int, input().split()))

	stack = []
	order = 0
	j = 1


	while j <= n:
		if len(trucks) > 0 and trucks[0] == j:
			del trucks[0]
			j+= 1
		elif len(stack) > 0 and stack[-1] == j:
			stack.pop()
			j+= 1
		elif len(trucks) > 0:
			stack.append(trucks.pop(0))
		else:
			break 

	print("yes" if len(stack) == 0 else "no")
