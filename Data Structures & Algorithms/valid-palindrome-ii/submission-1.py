class Solution:
    def isValid(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        while l<r:
            if s[l] != s[r]:
                #the two characters are not equal
                return self.isValid(s[l+1:r+1]) or self.isValid(s[l:r])
            l+=1
            r-=1
        return True

                
