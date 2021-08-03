n = int(input())

for i in range(n):
	expression = input()
	stack = []
	RPN = []

	for j in range(len(expression)):
		if expression[j].isalpha():
			RPN += expression[j]
		elif expression[j] in ["+", "-", "*", "/", "^"]:
			stack += expression[j]
		elif expression[j] == ")":
			RPN.append(stack[-1])
	print("".join(RPN))
