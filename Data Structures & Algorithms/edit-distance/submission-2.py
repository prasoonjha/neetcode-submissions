class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def edit(s, t):
            if (s,t) in cache:
                return cache[(s,t)]
            if not s:
                return len(t)
            if not t:
                return len(s)
            #if first chars are same recursive call on rest of strings
            if s[0] == t[0]:
                return edit(s[1:], t[1:])
            #only proceed if first chars are not the same
            insert = 1+edit(s, t[1:])
            replace = 1+edit(s[1:], t[1:])
            delete = 1+edit(s[1:], t)
            minDistance = min(insert, replace, delete)
            cache[(s,t)] = minDistance
            return minDistance

        return edit(word1, word2)