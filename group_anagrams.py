"""
Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


def group_anagrams(string):
    word = {}
    for s in string:
        key = ''.join(sorted(s))
        if key in word:
            word.get(key).append(s)
        else:
            word[key] = [s]
    return word.values()


# using defaultdict
from collections import defaultdict
def group_anagrams_2(string):
    word = defaultdict(list)
    for st in string:
        s = ''.join(sorted(s))
        word[s].append(st)
    return word.values()
