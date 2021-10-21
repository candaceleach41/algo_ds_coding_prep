"""
Given a string expression of numbers and operators, return all possible results from computing all the
different possible ways to group numbers and operators. You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""


def diff_ways_to_compute(expression):
    result = []

    # if the expression is a digit, return that digit (as an integer)
    if expression.isdigit():
        return [int(expression)]

    for i in range(len(expression)):
        if expression[i] in "+-*":
            left = diff_ways_to_compute(expression[:i])
            right = diff_ways_to_compute(expression[i + 1:])
            for j in left:
                for k in right:
                    result.append(operators(j, k, expression[i]))

    return result


# need to find a way to turn the operators from a string to an actual operator
def operators(left, right, op):
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    if op == "*":
        return left * right
