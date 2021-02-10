import heapq


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []
        count = 0
        while count < len(heights) - 1:
            dif = heights[count + 1] - heights[count]
            if dif > 0:
                heapq.heappush(heap, dif)
                if ladders < len(heap):
                    bricks = bricks - heapq.heappop(heap)
                    if bricks < 0:
                        return count
            count += 1
        return count


obj = Solution()
print(obj.furthestBuilding([1, 5, 2, 3, 4], 4, 1))
