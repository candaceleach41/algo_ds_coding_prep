"""
Given a string s, return the first non-repeating character in it
and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
"""


# Time O(1) | Space O(1)
def first_uniq_char(string):
    visited = set()
    for i in range(len(string)):
        if string[i] not in visited:
            visited.add(string[i])
            if string.count(string[i]) == 1:
                return i
    return -1


if __name__ == "__main__":
    print(first_uniq_char("hello"))
    print(first_uniq_char("upupdowndownleftrightleftrightbastart"))
    print(first_uniq_char("ha"))