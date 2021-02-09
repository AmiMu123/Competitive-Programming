class Solution:
    def lastStoneWeight(self, stones):
        sorted_stones = sorted(stones)
        while len(sorted_stones) > 1:

            if sorted_stones[len(sorted_stones)-1] != sorted_stones[len(sorted_stones)-2]:
                new_weight = sorted_stones[len(
                    sorted_stones)-1] - sorted_stones[len(sorted_stones)-2]
                sorted_stones.pop()
                sorted_stones.pop()
                sorted_stones.append(new_weight)
                sorted_stones.sort()
            else:
                sorted_stones.pop()
                sorted_stones.pop()
        if len(sorted_stones) == 0:
            return 0
        return sorted_stones[0]


a = Solution()
print(a.lastStoneWeight([1, 1, 2, 2, 2, 1, 2, 12, 213, 232, 123, 111, 111]))

# [1, 1, 2, 2, 2, 1, 2, 12, 213, 232, 123, 111, 111]
