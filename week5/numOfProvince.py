class Solution:
    def findCircleNum(self, isConnected):
        len_m = len(isConnected)
        visited = set()
        count = 0

        def dfs(i):
            for j in range(len_m):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        for i in range(len_m):
            if i not in visited:
                dfs(i)
                count += 1
        return count
