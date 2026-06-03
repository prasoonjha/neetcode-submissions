class Solution:
    def getVector(self, s: str) -> List[Int]:
        _map = [0]*26
        for c in s:
            _map[ord(c)-ord('a')]+=1
        return _map
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        
        """
        _map1 = self.getVector(s1)
        n1 = len(s1)
        n2 = len(s2)
        start = 0
        window_vector = [0]*26
        for end in range(n2):
            end_c = s2[end]
            idx = ord(end_c)-ord("a")
            window_vector[idx] +=1
            while window_vector[idx] > _map1[idx] :
                window_vector[ord(s2[start])-ord("a")] -= 1
                #shrink the window
                start+=1
            #process the window
            if window_vector == _map1:
                return True

        return False
