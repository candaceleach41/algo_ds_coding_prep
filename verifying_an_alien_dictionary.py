"""
In an alien language, surprisingly they also use english lowercase letters, but possibly
in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien
language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence
the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter
(in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅',
where '∅' is defined as the blank character which is less than any other character.
"""

# Time: O(nm) - n is the length of order and m is the total number of characters in words
# Space: O(1) - The only extra DS is the hashtable to store the letters
def is_alien_sorted(words, order):
    alpha = {order[i]: i for i in range(len(order))}
    for i in range(1, len(words)):
        a, b = words[i - 1], words[i]
        for j in range(len(a)):
            if j == len(b):
                return False
            a_char, b_char = a[j], b[j]
            a_idx, b_idx = alpha[a_char], alpha[b_char]
            if a_idx < b_idx:
                break
            if a_idx > b_idx:
                return False
    return True
