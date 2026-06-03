class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        cache = {}
        def dfs(amount, i):
            if amount == 0:
                return 1 
            if i>=n:
                return 0
            if (amount, i) in cache:
                return cache[(amount, i)]
            #for each coin call dfs
            #choose ith coin
            l, r = 0, 0
            if amount-coins[i]>=0:
                l = dfs(amount-coins[i], i)
                r = dfs(amount, i+1)
            #skip ith coin
            #cache
            cache[(amount, i)] = l+r
            return l+r
        
        return dfs(amount, 0)



        """
        recursive soln(inefficient) #with mutating global res variable (bad for dp:( )
        def change(self, amount: int, coins: List[int]) -> int:
        res= 0 
        n = len(coins)
        def dfs(amount, i):
            nonlocal res
            if amount == 0:
                res+=1
                return 
            if i>=n:
                return
            #for each coin call dfs
            #choose ith coin
            if amount-coins[i]>=0:
                dfs(amount-coins[i], i)
            #skip ith coin
            dfs(amount, i+1)

        dfs(amount, 0)
        return res

        #without mutating global res variable (good for dp :|)

        def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        def dfs(amount, i):
            if amount == 0:
                return 1 
            if i>=n:
                return 0
            #for each coin call dfs
            #choose ith coin
            l, r = 0, 0
            if amount-coins[i]>=0:
                l = dfs(amount-coins[i], i)
                r = dfs(amount, i+1)
            #skip ith coin
            return l+r
        
        return dfs(amount, 0)
        """