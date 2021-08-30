"""
Given an array of integers temperatures represents the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the ith day to get a warmer
temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            result[cur] = i - cur
        stack.append(i)

    return result


# ---------------------------------Another Solution ----------------------------
def daily_temp(temperatures):
    warmer = [0] * len(temperatures)
    right_max = float('-inf')
    for i in range(len(temperatures) - 1, -1, -1):
        if temperatures[i] >= right_max:
            right_max = temperatures[i]
        else:
            if temperatures[i + 1] > temperatures[i]:
                warmer[i] = 1
            else:
                warmer_next = 1 + warmer[i + 1]
                while temperatures[i + warmer_next] <= temperatures[i]:
                    warmer_next += warmer[i + warmer_next]
                warmer[i] = warmer_next
    return warmer
