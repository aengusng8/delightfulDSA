molecule = input().strip()
mass = lambda c : 1 if c == "H" else 16 if c == "O" else 12  
stack = []

for c in molecule:
	if c.isalpha():
		stack.append(mass(c))
	elif c == "(":
		stack.append(-1)
	elif c == ")":
		temp = 0
		while stack[-1] != -1:
			temp += stack.pop()
		stack.pop()
		stack.append(temp)
	elif c.isnumeric():
		stack.append(stack.pop() * int(c))

print(sum(stack))
