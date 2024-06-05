#Task 2

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

input_data = open("input2.txt", "r")
output_data = open("output2.txt", "w")

N, M = map(int, input_data.readline().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input_data.readline().split())
    edges.append((w, u - 1, v - 1))
edges.sort()

uf = UnionFind(N)
total_cost = 0
for w, u, v in edges:
    if uf.find(u) != uf.find(v):
        uf.union(u, v)
        total_cost += w

output_data.write(str(total_cost))

input_data.close()
output_data.close()