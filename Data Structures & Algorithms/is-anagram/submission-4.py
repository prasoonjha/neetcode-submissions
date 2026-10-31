class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def vectorize(s):  
            vector = [0]*26
            for c in s:
                vector[ord(c)-ord("a")] +=1
            return vector
        vectors = vectorize(s)
        vectort = vectorize(t)
        return vectors == vectort
