"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the
intervals in the input.



Example 1:

    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    [  1, 3 ]                   [ 8, 10 ]                   [   15, 18  ]
       [    2, 6    ]


Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


# Time: O(n log n) - sorting based on the start 
# Space: O(n) - additional space to store the results
def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals

    result = []
    for interval in sorted(intervals, key=lambda x: x[0]):
        if result and interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result



def merge_intervals_2(intervals):
    if not intervals:
        return 0

    intervals.sort()
    res = []
    last = intervals[0]
    for cur in intervals:
        if cur[0] <= last[1]:
            last[1] = max(last[1], cur[1])
        else:
            res.append(last)
            last = cur
    res.append(last)
    return res


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals_2([[1, 3], [2, 6], [8, 10], [15, 18]]))
