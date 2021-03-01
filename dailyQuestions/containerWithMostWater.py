class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            if height[i] <= height[j]:
                maxArea = max(maxArea, height[i] * (j - i))
                i += 1
            if height[i] >= height[j]:
                maxArea = max(maxArea, height[j] * (j - i))
                j -= 1
        return maxArea
