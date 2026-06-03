class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        k_closest = []
        for x,y in points:
            dist = (x**2 + y**2)**(1/2)
            heapq.heappush(heap, (-dist,(x,y)))
            while len(heap) > k:
                heapq.heappop(heap)
        for _ in range(len(heap)):
            dist, (x, y) = heapq.heappop(heap)
            k_closest.append((x,y))
        return k_closest