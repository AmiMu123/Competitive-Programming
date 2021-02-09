import heapq


class KthLargest:

    def __init__(self, k, nums):
        nums = heapq.nlargest(k, nums)
        heapq.heapify(nums)
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
        # heapq.heapify(ans)
        # print(ans)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
