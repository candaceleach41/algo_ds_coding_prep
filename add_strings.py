"""
Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.


Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


# Time: O(n)
# Space: O(n)
def add_string(num1, num2):
    # Going to make num1 and num2 into a list since a stack is being used
    num_1 = list(num1)
    num_2 = list(num2)

    # adding the carry and result will start with an empty string
    carry = 0
    result = ''

    # perform a while loop long as there is a carry and both numbers available
    while carry or num_1 or num_2:
        if num_1:
            carry += int(num_1.pop())
        if num_2:
            carry += int(num_2.pop())
        result += str(carry % 10)
        carry //= 10

    return result[::-1]  # reverse the result


if __name__ == "__main__":
    print(add_string("11", "123"))
