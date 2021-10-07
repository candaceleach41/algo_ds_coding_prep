"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take
course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also
have finished course 1. So it is impossible.
"""


def can_finish(self, num_courses, prerequisites):
    set_map = {i: [] for i in range(num_courses)}

    for u, v in prerequisites:
        set_map[v].append(u)

    visit = set()

    def dfs(crs):
        if crs in visit:
            return False
        if not set_map[crs]:
            return True

        visit.add(crs)

        for prereq in set_map[crs]:
            if not dfs(prereq):
                return False

        visit.remove(crs)
        set_map[crs] = []
        return True

    for num in range(num_courses):
        if not dfs(num):
            return False
    return True
