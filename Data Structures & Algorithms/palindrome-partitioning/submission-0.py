class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<=r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def dfs(i,curr):
            if i == n:
                res.append(curr)
                return
            for j in range(i, n):
                if self.isPalindrome(s[i:j+1]):
                    dfs(j+1, curr+[s[i:j+1]])
              
        dfs(0,[])
        return res