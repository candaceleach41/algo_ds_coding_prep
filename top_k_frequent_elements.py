"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

# Time: O(n log(k))
# Space: O(n)
from heapq import heappush, heappop


def top_k_frequent(nums, k):
    if len(nums) == 1:
        return [nums[0]]

    # key (nums) value (num of freq)
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    # insert k items into heap
    heap = []
    for key in freq_dict:
        heappush(heap, (freq_dict[key], key))
        if len(heap) > k:
            heappop(heap)

    res = []
    while heap:
        freq, item = heappop(heap)
        res.append(item)
    return res


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [2, 1]
    print(top_k_frequent([1], 1))  # [1]
