class Solution:
    """
    "neetcode"
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        substrings = []
        curr = ""
        cache = {}
        def dfs(i):
            """
            recursive function that takes i 
            return void
            """
            if i==n:
                return True
            if i in cache:
                return cache[i]
            for j in range(i,n):
                curr_str = s[i:j+1]
                if curr_str in wordDict:
                    #i->j is in dictionary, find if remaining words are in
                    if dfs(j+1):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return dfs(0)