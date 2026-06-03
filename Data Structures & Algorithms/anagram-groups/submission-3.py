from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # alphabets = {chr(i): (i - 97) for i in range(97, 123)}
        # rec_map = {}
        # res = []
        # for curr_string in strs:
        #     idt_filter = [0]*26 
        #     for char in curr_string:
        #         #switch on the corresponding bit in filter
        #         idt_filter[ord(char)-ord("a")] += 1
                
        #     #add the element to record map
        #     rec_map[curr_string] = idt_filter
        #     #reset filter
            

        # #iterate through items.vals and group equals together   
        # #even if there id only one entry, add it to a list   
        # # for k, v in rec_map.items():
        # #group keys with similar values

        # groups = defaultdict(list)
        
        # for word, vector in rec_map.items():
        #     groups[tuple(vector)].append(word)
        # res = list(groups.values())

        res = defaultdict(list)
        #iterate through the list strs
        for word in strs:
            #a vector for each word
            vector = [0]*26

            for c in word:
                #update each char's frequency
                vector[ord(c)-ord('a')] += 1
            
            res[tuple(vector)].append(word)

        print(res.values())

        return list(res.values())
                