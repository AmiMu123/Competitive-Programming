class Solution:
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                count += len(grid[0]) * (len(grid) - i)
                break
            elif grid[i][-1] >= 0:
                continue
            left = 0
            right = len(grid[i])-1
            while left <= right:
                mid = (left + right) // 2
                if grid[i][mid] < 0:
                    if grid[i][mid-1] >= 0:
                        break
                    right = mid - 1
                elif grid[i][mid] >= 0:
                    if grid[i][mid+1] < 0:
                        mid += 1
                        break
                    left = mid + 1
            count += len(grid[i]) - mid
        return count
