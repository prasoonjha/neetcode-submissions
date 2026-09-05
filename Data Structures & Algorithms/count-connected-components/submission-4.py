class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n

    def find(self, x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return 0
        if self.rank[a]>self.rank[b]:
            self.parent[b] = a
        elif self.rank[b]>self.rank[a]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            self.rank[a] +=1
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u,v in edges:
            res-=dsu.union(u,v)
        return res

