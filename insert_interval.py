"""
Given a set of non-overlapping intervals, insert a new interval into the intervals
(merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


# Time: O(n log n) - sorting by start (interval[0])
# Space: O(n) - storing merge result
def insert(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])

    res = []
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res


# Another solution, using O(n) time
def insert_2(intervals, new_interval):
    res = []
    new = new_interval

    for idx, i in enumerate(intervals):
        if i[1] < new[0]:
            res.append(i)
        elif new[1] < i[0]:
            res.append(new)
            return res + intervals[idx:]
        else:
            new[0] = min(new[0], i[0])
            new[1] = max(new[1], i[1])
    res.append(new)
    return res


if __name__ == "__main__":
    print(insert([[1, 3], [6, 9]], [2, 5]))
    print(insert_2([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
