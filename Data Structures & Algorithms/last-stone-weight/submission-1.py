class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        n = len(stones)
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap)>1:
            top = heapq.heappop(heap)
            _next = heapq.heappop(heap)
            if top != _next:
                new_stone = abs(top)-abs(_next)
                heapq.heappush(heap, -new_stone)
        return -heapq.heappop(heap) if len(heap) == 1 else 0
        #stones in the pile are not sorted, store them in a heap
        #then keep popping until stones>=1
        #
        