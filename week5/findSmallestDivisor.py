from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)
        ans = None
        while left <= right:
            mid = left + (right - left)//2
            nums_sum = 0
            for value in nums:
                val = ceil((value/mid))
                nums_sum += val
            if nums_sum <= threshold:
                ans = mid
                right = mid-1
            else:
                left = mid + 1
        return ans
