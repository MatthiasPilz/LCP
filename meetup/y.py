class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])

        ans = []
        # initialise the color list
        color = [0 for _ in range(numCourses)]

        def dfs(v):
            color[v] = 1
            for u in adj[v]:
                if color[u] == 0:
                    return dfs(u)
                else:
                    return True

            ans.append(v)
            return False

        def findCycle() -> bool:
            color = [0 for _ in range(numCourses)]
            for i in range(numCourses):
                if color[i] == 0:
                    if dfs(i):
                        return True
            return False

        def topological_sort():
            color = [0 for _ in range(numCourses)]
            for i in range(numCourses):
                if color[i] == 0:
                    dfs(i)

            ans.reverse()
            return ans

        if not findCycle():
            return topological_sort()
        else:
            return []



s = Solution()
print(s.findOrder(2, [[1,0]]))
