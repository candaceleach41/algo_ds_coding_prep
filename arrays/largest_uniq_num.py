"""
Given an array of integers A, return the largest integer that
only occurs once.

If no integer occurs once, return -1.



Example 1:
Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation:
The maximum integer in the array is 9 but it is repeated.
The number 8 occurs only once, so it's the answer.

Example 2:
Input: [9,9,8,8]
Output: -1
Explanation:
There is no number that occurs only once.
"""


def largest_unique_num(A):
    answer = -1
    visited = {}

    for i in A:
        if i not in visited:
            visited[i] = 1
        else:
            visited[i] += 1

    for k, v in visited.items():
        if v == 1:
            answer = max(k, answer)
    return answer


if __name__ == "__main__":
    print(largest_unique_num([5, 7, 3, 9, 4, 9, 8, 3, 1]))
