fre_x = [False] * (10 ** 6 + 5)
fre_y = [False] * (10 ** 6 + 5)
unique_x = []
unique_y = []
points = []

for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))

    if not fre_x[x]:
        fre_x[x] = True
        unique_x.append(x)
    
    if not fre_y[y]:
        fre_y[y] = True
        unique_y.append(y)

if len(unique_x) != 3 or len(unique_y) != 3:
    print('ugly')
    exit()

unique_x.sort()
unique_y.sort()
points.sort()
index = 0

for i in range(3):
    for j in range(3):
        if i == j == 1:
            continue
        if unique_x[i] == points[index][0] and unique_y[j] == points[index][1]:
            index += 1
        else:
            print('ugly')
            exit()

print('respectable')

