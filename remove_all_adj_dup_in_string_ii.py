def remove_all_adj_dup(s, k):
    stack = []

    for char in s:
        if not stack or stack[-1][0] != char:
            stack.append([char])
        elif stack[-1][0] == char:
            if len(stack[-1]) == k - 1:
                stack.pop()
            else:
                stack[-1].append(char)
    return "".join("".join(i) for i in stack)
