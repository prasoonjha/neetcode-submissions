class Solution:
    #AAABABB
    # start = 0, end = 0 char[end] = "A" map={A:1} max_len = 1
    # start = 0, end = 1             "A" map={A:2} max_len = 2
    # start = 0, end = 2             "A" map={A:3} max_len = 3
    # start = 0, end = 3             "B" map={A:3,B:1} max_len = 4
    #            end = 4             "A" map={A:4,B:1} max_len = 5
    # start =0,      = 5             "B" map={A:4,B:2} max_len = 
    def characterReplacement(self, s: str, k: int) -> int:
       
       count_map = {}
       start = 0
       longest = -1
       for end in range(len(s)):
            char = s[end]

            #add to count_map
            if char in count_map:
                count_map[char] += 1
            else:
                count_map[char] = 1

            
            while start<=end and count_map and end-start+1-max(count_map.values())>k:
                #shrink
                #remove char from map
                
                if count_map[s[start]]>1:
                    count_map[s[start]] -= 1
                else:
                    del count_map[s[start]]
                start+=1

            longest = max(longest, end-start+1)
       return longest

         