"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

import heapq


# Time: O(n log n) - sorting based on start time (intervals[0])
# Space: O(n): - storing the end time in the heap
def min_meeting_rooms(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    heap = []  # stores the end time of intervals

    for start, end in intervals:
        if heap and heap[0] <= start:
            # means two intervals can use the same room
            heapq.heapreplace(heap, end)
        else:
            # a new room is allocated
            heapq.heappush(heap, end)
    return len(heap)



if __name__ == "__main__":
    print(min_meeting_rooms([[0, 30], [5, 10], [15, 20], [9, 16], [11, 14]]))
