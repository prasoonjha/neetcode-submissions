class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vector_s = [0]*26
        vector_t = [0]*26
        for c in s:
            idx = ord(c)-ord("a")
            vector_s[idx] +=1
        for c in t:
            idx = ord(c)-ord("a")
            vector_t[idx] +=1

        return vector_s == vector_t