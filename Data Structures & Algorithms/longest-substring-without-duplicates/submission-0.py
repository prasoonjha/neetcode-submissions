class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        found = set()
        longest = 0
        for end in range(len(s)):
            while start<=end and s[end] in found:
                found.remove(s[start])
                start+=1
            
            longest = max(longest, end-start+1)
            found.add(s[end])
            

        return longest