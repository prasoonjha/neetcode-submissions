class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = -1
        i = 0
        n = len(strs)
        #the longest common prefix can only be as long as the shortest word
        longest_possible = float('inf')
        for word in strs:
            longest_possible = min(len(word), longest_possible)
        longest = ""
        print("lp:",longest_possible)
        for i in range(longest_possible):
            #check if all the chars at index i in each word is the same,
            #if same, append to result string, else break and return longest so far
            char_set = set()
            char_i = None
            for word in strs:
                char_i = word[i]
                char_set.add(char_i)
            if len(char_set) == 1:
                #all chars at ith pos were same
                longest+=char_i
            else:
                break
        return longest