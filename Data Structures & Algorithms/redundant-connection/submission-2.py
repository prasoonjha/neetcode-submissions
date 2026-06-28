class Solution:
    
            
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n= len(edges)
        dsu = DSU(n)
        for n1, n2 in edges:
            if not dsu.union(n1-1, n2-1):
                return [n1, n2]

class DSU:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.rank = [1]*(n)

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x,y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            rx, ry = self.rank[px], self.rank[py]

            if rx>ry:
                self.parent[py] = px
            elif rx<ry:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] +=1
            return True