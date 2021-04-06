"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

# Time: O(n) N is the length of the string
# Space O(n) 
def decode_string(string):
    stack = []
    cur_num = 0
    cur_string = ""

    for char in string:
        if char == '[':
            stack.append(cur_string)
            stack.append(cur_num)
            cur_string = ""
            cur_num = 0
        elif char == ']':
            num = stack.pop()
            prev_string = stack.pop()
            cur_string = prev_string + num * cur_string
        elif char.isdigit():
            cur_num = cur_num * 10 + int(char)
        else:
            cur_string += char
    return cur_string


if __name__ == "__main__":
    print(decode_string("3[a]2[bc]"))
    print(decode_string("abc3[cd]xyz"))
