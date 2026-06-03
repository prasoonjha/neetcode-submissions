class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for prereq in prerequisites:
            u,v = prereq
            adj[u].append(v)
        def topo(adj, n):
            order = []
            indeg = [0] * n
            for u in range(n):
                for v in adj[u]:
                    indeg[v] +=1
            q = deque([i for i in range(n) if indeg[i]==0])
            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    indeg[nei] -=1
                    if indeg[nei] == 0:
                        q.append(nei)
            return order[::-1]
        order=topo(adj, numCourses)
        return order if len(order) == numCourses else []