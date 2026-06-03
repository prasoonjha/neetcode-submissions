from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force
        #create a map
        freq_map = Counter(nums).most_common()
        res = []
        for key, vals in dict(freq_map).items():
            if k>0:
                res.append(key)
            else:
                break
            k-=1
        return res