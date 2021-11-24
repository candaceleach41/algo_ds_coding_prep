"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""


# Two pointer approach
# Time O(n)
# Space O(1)
def trappng_rain_water(heights):
    n = len(heights)
    if n <= 2:
        return 0

    max_left = heights[0]
    max_right = heights[n - 1]
    trapped_water = 0
    left = 1
    right = n - 2

    while left <= right:
        if max_left < max_right:
            if heights[left] > max_left:
                max_left = heights[left]
            else:
                trapped_water += max_left - heights[left]
            left += 1
        else:
            if heights[right] > max_right:
                max_right = heights[right]
            else:
                trapped_water += max_right - heights[right]
            right -= 1
    return trapped_water
