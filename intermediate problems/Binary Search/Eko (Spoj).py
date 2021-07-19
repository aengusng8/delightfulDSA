def Check(trees, mid):
	Sum = 0
	for tree in trees:
		Sum += max(0, tree - mid)
	return Sum

def binary_search(trees, left, right, M):
	while left <= right:
		mid = (left + right) // 2

		if Check(trees, mid) >= M:
			ans = mid
			left = mid + 1
		else:
			right = mid - 1

	return int(ans)

nTrees, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = 1e9

print(binary_search(trees, left, right, M))
