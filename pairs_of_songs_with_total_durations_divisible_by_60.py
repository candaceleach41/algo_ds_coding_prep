"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds
is divisible by 60. Formally, we want the number of indices i, j such that
i < j with (time[i] + time[j]) % 60 == 0.


Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""

"""
This problem has a bit of a similarity to the Two-Sum problem except (x + y) % z == 0
"""

from collections import Counter, defaultdict

from numpy import mod


# This one is using a Map and Counter
# consider using the first half for calculation to avoid duplicates (hence, edge cases)
def pairs_div_by_60(time):
    rem = map(mod, time, [60] * len(time))
    c = Counter(rem)

    count = 0
    # Edge cases to handle 0 and 30
    count += (c[0] - 1) * c[0] // 2
    count += (c[30] - 1) * c[30] // 2

    for i in range(30):
        count += c[i] * c[60 - i]

    return count


# Another version of the solution
def pairs_div_by_60_v2(time):
    rem = defaultdict(int)
    count = 0

    for song in time:
        if song % 60 == 0:
            count += rem[0]
        else:
            count += rem[60 - song % 60]
        rem[song % 60] += 1

    return count


if __name__ == "__main__":
    print(pairs_div_by_60([30, 20, 150, 100, 40]))
    print(pairs_div_by_60_v2([30, 20, 150, 100, 40]))
