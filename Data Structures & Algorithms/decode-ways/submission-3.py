class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        char_map = {}
        for i in range(26):
            character = ord('A')
            char_map[chr(i+character)] = str(i+1)

        cache = {}
        def dfs(i):

            #base case
            if i == n:
                return 1
            if i in cache:
                return cache[i]
            num_ways = 0
            for j in range(i, n):
                curr_num = s[i:j+1]
                
                if curr_num in char_map.values():
                    res = dfs(j+1)
                    num_ways+=res
            cache[i] = num_ways
            return num_ways
                
        return dfs(0)



"""
simple recursive soln
def numDecodings(self, s: str) -> int:
        n = len(s)
        char_map = {}
        for i in range(26):
            character = ord('A')
            char_map[chr(i+character)] = str(i+1)

        num_ways = 0
        def dfs(i):
            nonlocal num_ways
            #base case
            if i == n:
                return 1
            
            for j in range(i, n):
                curr_num = s[i:j+1]
                if curr_num in char_map.values():
                    res = dfs(j+1)
                    if res == 1:
                        num_ways+=1
            return 0
                
        dfs(0)
        return num_ways

"""
