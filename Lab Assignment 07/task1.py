#Task 1

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

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
            self.size[x_root] += self.size[y_root]
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
        return self.size[x_root]

input_data = open("input1.txt", "r")
output_data = open("output1.txt", "w")

N, K = map(int, input_data.readline().split())
uf = UnionFind(N + 1)
for _ in range(K):
    A, B = map(int, input_data.readline().split())
    circle_size = uf.union(A, B)
    output_data.write(str(circle_size) + "\n")

input_data.close()
output_data.close()