"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line = [(interval.start, 1) for interval in intervals]+[(interval.end, -1) for interval in intervals]
        count = 0
        ans = 0
        for ele in sorted(line):
            if ele[1]>0:
                count+=1
            elif ele[1]<0:
                count-=1
            print(count)
            ans = max(ans, count)
        return ans

        # 0,5,10,15,40,20

        # 1,2,1,2,1,0