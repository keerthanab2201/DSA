"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start) # first sort the array according to start times
        '''each meeting needs a room from its start time to its end time
if a meeting starts after or at the same time another meeting ends, they can share the same room
otherwise, we need a new room'''
        minheap=[] # stores end times of currently running meetings- top is the room that frees up earliest
        rooms=0
        for i in intervals:
            if minheap and minheap[0]<=i.start:
                heapq.heappop(minheap)
            else:
                rooms+=1
            heapq.heappush(minheap,i.end)
        return rooms
                
