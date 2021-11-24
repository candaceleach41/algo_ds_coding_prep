"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i
such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Example 4:
Input: arr = [3,4,5,1]
Output: 2

Example 5:
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2

Constraints:
3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""


# Using Linear Search
def peak_idx_mount_array(arr):
    if len(arr) < 3:
        return 0

    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            return i


# Using Binary Search
def peak_idx_mount_arr_bs(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        high = mid
    return low


if __name__ == "__main__":
    print(peak_idx_mount_arr_bs([24, 69, 100, 99, 79, 78, 67, 36, 26, 1, 9]))
    print(peak_idx_mount_array([1, 10, 5, 2]))
    print(peak_idx_mount_array([1, 75, 55, 2]))
