"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        min_rooms, rooms = 0, 0
        start, end = sorted([interval.start for interval in intervals]), sorted([interval.end for interval in intervals])
        s, e = 0, 0
        
        while s<n:
            if start[s]<end[e]:
                print("meeting started", start[s])
                rooms+=1
                s+=1
            else:
                print("meeting ended", end[e])
                #decrement count
                rooms-=1
                #move e ahead
                e+=1
            
            min_rooms = max(min_rooms, rooms)
        return min_rooms
        