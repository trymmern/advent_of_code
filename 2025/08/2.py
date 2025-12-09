from math import sqrt

f = open("input.txt", "r")

points = [(int(x), int(y), int(z)) for x, y, z in (line.strip().split(",") for line in f)]
print(points)

class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n))
    self.size = [1] * n

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x == root_y:
      return
    
    if self.size[root_x] < self.size[root_y]:
      self.parent[root_x] = root_y
      self.size[root_y] += self.size[root_x]
    else:
      self.parent[root_y] = root_x
      self.size[root_x] += self.size[root_y]
  
  def get_sizes(self):
    size_count = {}
    for i in range(len(self.parent)):
      root = self.find(i)
      if root not in size_count:
        size_count[root] = 0
      size_count[root] += 1
    return list(size_count.values())
  
  def count(self):
    roots = set()
    for i in range(len(self.parent)):
      roots.add(self.find(i))
    return len(roots)

# Euclidean distance in 3D: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
def euclidean_dist(p1, p2):
  return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

pairs = []
for i in range(len(points)):
  for j in range(i+1, len(points)):
    dist = euclidean_dist(points[i], points[j])
    pairs.append((dist, i, j))

pairs.sort()
uf = UnionFind(len(points))
iterator = 0
current_pair = (0, 0, 0)
while uf.count() > 1:
  dist, i, j = pairs[iterator]
  current_pair = (dist, i, j)
  uf.union(i, j)
  iterator += 1

x1 = points[current_pair[1]][0]
x2 = points[current_pair[2]][0]
result = x1 * x2
print("Result:", result)
