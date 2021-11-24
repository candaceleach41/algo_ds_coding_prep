"""
You have n processes forming a rooted tree structure. You are given two integer arrays pid and
ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent
process.

Each process has only one parent process but may have multiple children processes. Only one
process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return a list of the
IDs of the processes that will be killed. You may return the answer in any order.

Example 1:

                                    3
                                /      \
                              1         5   <----
                                       /        |--- Kill
                                     10     <---

Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.
Example 2:

Input: pid = [1], ppid = [0], kill = 1
Output: [1]
"""

from collections import defaultdict, deque
def kill_process(pid, ppid, kill):
    node_dic = defaultdict(list)
    for i, pp in enumerate(ppid):
        node_dic[pp].append(pid[i])

    result = []
    queue = deque([kill])
    while queue:
        parent_node = queue.popleft()
        result.append(parent_node)

        queue.extend(node_dic[parent_node])
    return result
