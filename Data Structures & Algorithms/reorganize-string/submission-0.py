class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        freq = Counter(s)
        freq_heap = [(-cnt, char) for char, cnt in freq.items()]
        heapq.heapify(freq_heap)

        while len(freq_heap)>1:
            
            cnt1, char1 = heapq.heappop(freq_heap)
            cnt2, char2 = heapq.heappop(freq_heap)
            res+=[char1, char2]
            if cnt1+1: heapq.heappush(freq_heap, (cnt1+1, char1))
            if cnt2+1: heapq.heappush(freq_heap, (cnt2+1, char2))
            #this char could have been used last, or not
        if freq_heap:
            remaining_char_cnt, remaining_char = heapq.heappop(freq_heap)
            if remaining_char_cnt<-1:
                return ""
            res.append(remaining_char)
        
        return "".join(res)
                
                    
            