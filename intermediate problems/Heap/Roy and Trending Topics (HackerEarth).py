import heapq

class Topic:
	def __init__(self, _ID, _old_score, _new_score):
		self.ID = _ID
		self.old_score = _old_score
		self.new_score = _new_score
		self.change = self.new_score - self.old_score

	def __lt__(self, other):
		return (self.change > other.change) or (self.change == other.change and self.ID > other.ID)

n = int(input())
pq = []

for _ in range(n):
	ID, old_score, post, like, comment, share = map(int, input().split())
	new_score = post * 50 + like * 5 + comment * 10 + share * 20
	pq.append(Topic(ID, old_score, new_score))

heapq.heapify(pq)

for _ in range(5):
	t = heapq.heappop(pq)
	print(t.ID, t.new_score)
