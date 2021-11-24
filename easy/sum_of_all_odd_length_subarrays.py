"""
Given an array of positive integers arr, calculate the sum of all possible
odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:
Input: arr = [10,11,12]
Output: 66
"""


# time: O(n^2)
# Space: O(1)
def sum_of_all_off_len_subarrays(arr):
    result = 0

    for i in range(len(arr)):
        for j in range(i, len(arr), 2):
            result += sum(arr[i:j + 1])
    return result


# Time: O(n) - n is the length of the array
# Space: O(1) - not using extra storage
def sum_of_all_len_subarays_ii(arr):
    n = len(arr)
    start, end, total, sum_total = 0, 0, 0, 0
    i = 0
    while i < n:
        start = n - i
        end = i + 1
        total = start * end
        odd = total // 2
        if total % 2 == 1:
            odd += 1
        sum_total += odd * arr[i]
        i += 1
    return sum_total


# Time: O(n)
# Space: O(1)
def sum_of_all_off_len_subarrays_opt(arr):
    result = 0
    freq = 0
    n = len(arr)

    for i in range(n):
        freq = freq - (i + 1) // 2 + (n - i + 1) // 2
        result += freq * arr[i]
    return result


if __name__ == "__main__":
    print(sum_of_all_off_len_subarrays([1, 4, 2, 5, 3]))  # 58
    print(sum_of_all_off_len_subarrays_opt([3, 4, 5, 1, 8]))  # 78
