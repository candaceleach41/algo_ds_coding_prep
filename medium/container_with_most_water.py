"""
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
"""


def max_area(height):
    start = 0
    end = len(height) - 1
    largest = 0
    prev_start = 0
    prev_end = 0

    while start != end:
        if height[start] < prev_start:
            start += 1
            continue

        if height[end] < prev_end:
            end -= 1
            continue

        next_area = min(height[start], height[end]) * (end - start)

        if next_area > largest:
            largest = next_area

        if height[start] < height[end]:
            prev_start = height[start]
            start += 1
        else:
            prev_end = height[end]
            end -= 1
    return largest


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
