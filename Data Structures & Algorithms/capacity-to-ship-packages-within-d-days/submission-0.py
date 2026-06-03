class Solution:
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shippable(capacity):
            num_days_required, curr_cap = 1, capacity
            
            for w in weights:
                if curr_cap-w < 0:
                    num_days_required+=1
                    curr_cap = capacity
                curr_cap -= w
            return num_days_required<= days
        
        l, r = max(weights), sum(weights)

        while l<=r:
            mid = (l+r)//2
            if shippable(mid):
                r = mid-1
            else:
                l = mid+1
        return l


