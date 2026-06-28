class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]*(n+1)
        outdegree= [0]*(n+1)
        for u, v in trust:
            indegree[v]+=1
            outdegree[u] +=1
        print(indegree)
        for person in range(1, n+1):
            if indegree[person] == n-1 and outdegree[person] == 0:
                return person
        return -1