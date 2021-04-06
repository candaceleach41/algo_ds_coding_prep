"""
Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


# Using Trie
def longest_common_prefix(strs):
    trie = {}
    for word in strs:
        cur_node = trie
        for char in word:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node['*'] = {}

    cur_node = trie
    cur_pre = ''
    while len(cur_node) == 1 and '*' not in cur_node:
        for key in cur_node:
            cur_node = cur_node[key]
            cur_pre += key
    return cur_pre


# This one is using set
def longest_common_prefix_set(strs):
    result = []
    for i in zip(*strs):
        if len(set(i)) == 1:
            result.append(i[0])
        else:
            break
    return "".join(result)


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix_set(["flower", "flow", "flight"]))
