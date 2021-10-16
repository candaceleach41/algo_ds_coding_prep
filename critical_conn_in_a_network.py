"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server
connections forming a network where connections[i] = [ai, bi] represents a connection
between servers ai and bi. Any server can reach other servers directly or indirectly
through the network.

A critical connection is a connection that, if removed, will make some servers unable to
reach some other server.

Return all critical connections in the network in any order.



                1 ------- 2
               | \        |
               |  \       |
               |   \      |
critical  ->   |    \     |
               |     \    |
               |      \   |
               3        0
Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]


Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from collections import defaultdict


def critical_connections(n, connections):
    num = 0
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    discover_num = [None] * n
    low = [None] * n

    def dfs(node, parent):
        # already visited
        nonlocal num
        if discover_num[node] is not None:
            return

        discover_num[node] = low[node] = num
        num += 1
        for neighbor in graph[node]:
            if discover_num[neighbor] is None:
                dfs(node, parent)

        # minimal number of neighbors, exclude the parent
        low[node] = min([discover_num[node]] + [low[neighbor] for neighbor in graph[node] if neighbor != parent])

    dfs(0, 0)

    result = []
    for u, v in connections:
        # non bridge
        if low[u] > discover_num[v] or low > discover_num[u]:
            result.append([u, v])
    return result


if __name__ == "__main__":
    print(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
