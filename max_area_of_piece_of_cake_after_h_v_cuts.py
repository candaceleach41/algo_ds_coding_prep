"""
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts
and verticalCuts where:

    - horizontalCuts[i] is the distance from the top of the rectangular cake to the ith
    horizontal cut and similarly, and
    - verticalCuts[j] is the distance from the left of the rectangular cake to the jth
    vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical
position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a
large number, return this modulo 109 + 7.


Example 1:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the
horizontal and vertical cuts. After you cut the cake, the green piece of cake has the
maximum area.

Example 2:
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the
horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake
have the maximum area.

Example 3:
Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
"""


# Naive approach (time limit exceeded): Time: O(m*n) Space: O(1)

def max_area(h, w, horizontal_cuts, vertical_cuts):
    horizontal_cuts = sorted(horizontal_cuts)
    vertical_cuts = sorted(vertical_cuts)

    horizontal_cuts.append(h)
    vertical_cuts.append(w)

    largest_area = 0
    prev_height = 0

    for hc in horizontal_cuts:
        prev_width = 0
        for vc in vertical_cuts:
            area = (hc - prev_height) * (vc - prev_width)
            largest_area = max(area, largest_area)
            prev_width = vc
        prev_height = hc
    return largest_area % 1000000007


# Optimized solution: Time: O(n log n) Space O(1)
def max_area_optimized(h, w, horizontal_cuts, vertical_cuts):
    horizontal_cuts = sorted(horizontal_cuts)
    vertical_cuts = sorted(vertical_cuts)

    horizontal_cuts.append(h)
    vertical_cuts.append(w)

    horizontal_cuts = [0] + horizontal_cuts
    vertical_cuts = [0] + vertical_cuts

    max_height, max_width, prev_height = 0, 0, 0,

    for i in range(1, len(horizontal_cuts)):
        max_height = max(horizontal_cuts[i] - horizontal_cuts[i-1], max_height)

    for j in range(1, len(vertical_cuts)):
        max_width = max(vertical_cuts[i] - vertical_cuts[i-1], max_width)
        prev_width = vertical_cuts

    return max_height * max_width % 1000000007
