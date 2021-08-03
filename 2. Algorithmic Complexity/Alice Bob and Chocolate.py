n = int(input())
bars = list(map(int, input().split()))
t_alice = t_bob = 0
i, j = 0, n - 1

while i <= j:
    if t_alice + bars[i] <= t_bob + bars[j]:
        t_alice += bars[i]
        i += 1
    else:
        t_bob += bars[j]
        j -= 1

print(i, n - i)
