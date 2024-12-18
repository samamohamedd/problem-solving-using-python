class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # x[2] is the weight
    uf = UnionFind(n)
    mst = []
    
    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, w))
            uf.union(u, v)
            if len(mst) == n - 1:  # Stop when MST has n-1 edges
                break
    return mst

# Example :
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

n = 4  # Number of vertices
mst = kruskal(n, edges)
print("Edges in the MST:")
for edge in mst:
    print(edge)

