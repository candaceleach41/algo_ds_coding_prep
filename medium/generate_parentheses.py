"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed
parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""


def generate_parenthesis(n):
    def backtrack(result, curr, open_paren, close_paren, max_paren):
        if len(curr) == 2 * max_paren:
            result.append(curr)
        if open_paren < max_paren:
            backtrack(result, curr + '(', open_paren + 1, close_paren, max_paren)
        if close_paren < open_paren:
            backtrack(result, curr + ')', open_paren, close_paren + 1, max_paren)

    result = []
    open_paren, close_paren = 0, 0
    curr = ''
    backtrack(result, curr, open_paren, close_paren, n)
    return result
