class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])

        def dfs(v, color) -> bool:
            color[v] = 1
            for u in adj[v]:
                if color[u] == 0:
                    return dfs(u)
                elif color[u] == 1:
                    return True

            color[v] = 2
            return False

        def findCycle() -> bool:
            # initialise the color list
            color = [0 for _ in range(numCourses)]
            for i in range(numCourses):
                if color[i] == 0:
                    print(color)
                    if dfs(i, color):
                        print("i: %d" %i)
                        return True
            return False

        print("Are there any cycles?")
        print(findCycle())

s = Solution()
s.findOrder(2, [[1,0]])