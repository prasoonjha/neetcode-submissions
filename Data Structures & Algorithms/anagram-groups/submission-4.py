class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        _map = defaultdict(list)
        for word in strs:
            vector = [0]*26
            for c in word:
                idx = ord(c) - ord("a")
                vector[idx] += 1
            _map[tuple(vector)].append(word)
        for k,v in _map.items():
            res.append(v)
        return res