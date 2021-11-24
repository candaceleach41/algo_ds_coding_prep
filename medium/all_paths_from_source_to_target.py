"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from
node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:

                0 --------> 1
                |           |
                |           |
                v           v
                2 --------> 3

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""


def all_paths_source_target(graph):
    queue = [[0]]
    res = []
    while queue:
        current = queue.pop(0)
        last = current[-1]
        if last == len(graph)-1:
            res.append(current)
        else:
            for i in graph[last]:
                temp = current+[i]
                queue.append(temp)
    return res