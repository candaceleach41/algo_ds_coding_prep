"""
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""


# Time: O(n log n) - sorting intervals based on start time (intervals[0])
# Space: O(1) - not using extra storage
def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


if __name__ == "__main__":
    print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))
    print(can_attend_meetings([[7, 10], [2, 4]]))
