class Solution:
    def dijkstra(self, adj, n, src):
        distance = [float("inf")] * (n+1)
        distance[src] = 0
        q = []
        heapq.heappush(q, (0, src))
        while q:
            dist, node = heapq.heappop(q)
            
            if dist > distance[node]:
                continue

            for nei_node, nei_dist in adj[node]:
                if dist + nei_dist < distance[nei_node]:
                    distance[nei_node] = dist + nei_dist
                    heapq.heappush(q, (distance[nei_node], nei_node))
        return distance
            
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for edge in times:
            u, v, t = edge
            adj[u].append((v,t))
        res = self.dijkstra(adj, n, k)
        res = res[1:]
        return -1 if float("inf") in res else max(res)