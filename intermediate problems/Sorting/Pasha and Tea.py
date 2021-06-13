n, w = map(int, input().split())
tea_cups = list(map(int, input().split()))

tea_cups.sort()

if 2* tea_cups[0] <= tea_cups[int(len(tea_cups) / 2)]:
	answer = 3 * n * tea_cups[0]
else:
	answer = tea_cups[int(len(tea_cups) / 2)] / 2 * 3 * n

if answer > w:
  answer = w

print(answer)
