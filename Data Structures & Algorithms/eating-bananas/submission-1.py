class Solution:
    def hoursAtRate(self, piles:List[int], r: int) -> int:
        """
        return number of hours required to finish the pile at rate r bananas/hr
        """
        hours = 0
        if len(piles) == 1:
            return piles[0]/r
        for pile in piles:
            if pile<=r:
                hours+=1
            else:
                hours+=int(pile/r)+1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles) #eating at rate r = 1 banana per hr
        l,r = 1, max_rate
        while l<=r:
            rate_ph_mid = int((l+r)/2)
            hrs_required = self.hoursAtRate(piles, rate_ph_mid)
            if hrs_required <= h:
                #check if we can do better
                #since we need to find out the minimum rate we can check 
                #if this condition is also satisfied for slightly less
                r = rate_ph_mid-1
            if hrs_required >h:
                #number of hrs required to finish at current rate is 
                #greater than maximum permissible h, so we need to 
                #increase the rate of eating bananas
                l = rate_ph_mid+1
            
        return l