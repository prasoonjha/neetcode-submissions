from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force
        #create a map
        # freq_map = Counter(nums).most_common()
        # res = []
        # for key, vals in dict(freq_map).items():
        #     if k>0:
        #         res.append(key)
        #     else:
        #         break
        #     k-=1

        #optimized
        """
        maintain a list of size k and keep only the k largest 
        elements encountered so far
        """
        n = len(nums)
        count =  {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num]+=1
        freq = [[] for _ in range(n+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

