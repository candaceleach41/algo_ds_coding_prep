def my_atoi(s):
    int_max = 2147483647
    int_min = -2147483648
    s = s.strip()
    if not s:
        return 0
    sign, i = 1, 0
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    result = 0
    while i < len(s):
        if not s[i].isdigit():
            break
        result = result * 10 + ord(s[i]) - ord('0')
        if result > int_max:
            break
        i += 1
    return min(max(sign * result, int_min), int_max)
