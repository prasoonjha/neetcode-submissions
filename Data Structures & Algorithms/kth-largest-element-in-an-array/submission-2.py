import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []   #initialize empty array
        for num in nums:
            # push each num into the heap
            heapq.heappush(heap, num)
            while len(heap)>k: #if len of heap is greater than k, pop from heap
                heapq.heappop(heap)
        #finally pop at last and return
        return heapq.heappop(heap)
        """
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
        """
        