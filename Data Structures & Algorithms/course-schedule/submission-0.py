class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for prereq in prerequisites:
            u, v  = prereq
            adj[u].append(v)
        # for k,v in adj.items():
        #     print(k,v)
        indeg = [0] * numCourses
        order = []
    
        for u in range(numCourses):
            for v in adj[u]:
                indeg[v] += 1
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indeg[nei] -=1
                if indeg[nei] == 0:
                    q.append(nei)
        # return order

        print(order[::-1])
        return len(order) == numCourses
