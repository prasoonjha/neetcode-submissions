class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for edge in times:
            src, destination, time = edge
            adj[src].append((destination, time))
        
        def djikstra(adj, src):
            dist = [float("inf")]*(n+1)
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                curr_dist, src = heapq.heappop(pq)
                if curr_dist>dist[src]:
                    continue
                for neighbor in adj[src]:
                    nei, nei_distance = neighbor
                    nei_distance = nei_distance+curr_dist
                    if nei_distance < dist[nei]:
                        dist[nei] = nei_distance
                        heapq.heappush(pq, (nei_distance, nei))
            return dist
        dist = djikstra(adj, k)
        dist = dist[1:]
        min_time = -1
        for d in dist:
            if d == float("inf"):
                return -1
            min_time = max(min_time,d)
            print(d)
            
        return min_time
