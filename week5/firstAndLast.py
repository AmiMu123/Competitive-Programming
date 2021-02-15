class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return [self.leftSearch(nums, 0, mid, target), self.rightSearch(nums, mid, len(nums)-1, target)]
        return [-1, -1]

    def leftSearch(self, nums, left, right, target):
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
                # if there is no other target number to the left side
            elif nums[mid - 1] < target:
                return mid
            else:
                right = mid - 1
        # return 0 in my worest case its at index 0
        return left

    def rightSearch(self, nums, left, right, target):
        while left < right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
                # if there is no other target to the right side of target
            elif nums[mid + 1] > target:
                return mid
            else:
                left = mid + 1
        return right


searchRange = Solution()
print(searchRange.searchRange([1, 1, 1, 1, 1, 1, 1, 1], 1))
