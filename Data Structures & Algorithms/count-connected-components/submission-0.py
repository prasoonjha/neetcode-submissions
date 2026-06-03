class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)
        res = 0
        visited = [False]*n
        def dfs(i):
            visited[i] = True
            for nei in adj[i]:
                if not visited[nei]:
                    dfs(nei)
                    visited[nei] = True
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res+=1
        return res