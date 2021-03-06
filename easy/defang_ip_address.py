"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""


def defang_ip_address(address):
    result = []
    for char in address:
        if char.isdigit():
            result.append(char)
        else:
            result.append('[.]')
    return "".join(result)


# ---------------------------------------
# Optimized Solution
def defang_ip_addr(address):
    return address.replace('.', '[.]')

if __name__ == "__main__":
    print(defang_ip_addr("255.255.255.0"))
