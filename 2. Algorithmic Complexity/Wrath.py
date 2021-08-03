n = int(input())
a = list(map(int, input().split()))

count = 0
j = n - 1
#j là giới hạn bắt đầu của một lần vả: j giúp chống lặp người đã bị giết.
#j phải luôn bé hơn i, vì người ở i chỉ vả được những người ở bên trái nó.
#last_kill_pos: là giới hạn kết thúc của một lần vả.


for i in range(n - 1, -1 , -1):
	j = min(i, j)
	last_kill_pos = max(0, i - a[i])

	if j > last_kill_pos:
		count += (j - last_kill_pos)
		j = last_kill_pos
    
print(n - count)
