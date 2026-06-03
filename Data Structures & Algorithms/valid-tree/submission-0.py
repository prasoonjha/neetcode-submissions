class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
            
        adj = defaultdict(list)
        for edge in edges:
            a, b = edge
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(root):
            visited = {root}
            stack = [root]
            while stack:
                node = stack.pop()
                for child in adj[node]:
                    if child not in visited:
                        visited.add(child)
                        stack.append(child)
            return len(visited) == n
            
        return dfs(0)