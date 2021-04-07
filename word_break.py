"""
Given a string s and a dictionary of strings wordDict, return true if s can
be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in
the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

def word_break(string, word_dict):
    cache = [False for x in range(len(string) + 1)]
    cache[0] = True

    for i in range(len(string) +1):
        for j in range(i):
            if cache[j] and string[j:i] in word_dict:
                cache[i] = True
                break
    return cache[-1]


if __name__ == "__main__":
    print(word_break("catsandog", ["cats","dog","sand","and","cat"]))
    print(word_break("applepenapple", ["apple","pen"]))
