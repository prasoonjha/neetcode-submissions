class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        resIdx = 0 # store l idx of res and return s[resIdx: resIdx+length]
        n = len(s)
        for i in range(n):
           #check odd length
           l, r = i, i
           while l>=0 and r<n:
            left, right = s[l], s[r]
            length = r-l+1
            if left == right:
                if length > max_length:
                    max_length = max(max_length, length)
                    resIdx = l
                l-=1
                r+=1
            else:
                #cannot be a palindrome, escape from loop
                break
                
           #check even length
           l, r = i, i+1
           while l>=0 and r<n:
            left, right = s[l], s[r]
            length = r-l+1
            if left == right:
                if length > max_length:
                    max_length = max(max_length, length)
                    resIdx = l
                l-=1
                r+=1
            else:
                #cannot be a palindrome, escape from loop
                break

        return s[resIdx:resIdx+max_length]