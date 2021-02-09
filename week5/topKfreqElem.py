import heapq


class Solution:
    def topKFrequent(self, nums, k):
        my_dict = dict()
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        heap = []
        ans = []
        for key, value in my_dict.items():
            heapq.heappush(heap, [-1*value, -1 * key])

        for i in range(k):
            ans.append(-1 * heapq.heappop(heap)[1])

        return ans


my_obj = Solution()
print(my_obj.topKFrequent([1, 1, 1, 1, 1, 2, 3, 3,
                           3, 3, 3, 4, 4, 4, 4, 21, 21, 12, 12, 12, ], 3))
