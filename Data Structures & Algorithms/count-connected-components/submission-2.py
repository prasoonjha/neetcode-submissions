class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent  = [i for i in range(n)]
        rank = [1]*n
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1]> rank[p2]:
                parent[p2] = p1
                rank[p2] += rank[p1]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for edge in edges:
            u, v = edge
            res -=union(u,v)
        return res