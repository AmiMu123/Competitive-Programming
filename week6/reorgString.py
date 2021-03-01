import heapq


class Solution:
    def reorganizeString(self, S) -> str:
        freq = Counter(S)
        heap = [(-v, k) for (k, v) in freq.items()]
        heapq.heapify(heap)
        result = []
        while len(heap) > 1:
            curr = heapq.heappop(heap)
            nxt = heapq.heappop(heap)
            result.extend([curr[1], nxt[1]])
            if curr[0] < -1:
                heapq.heappush(heap, (curr[0] + 1, curr[1]))
            if nxt[0] < -1:
                heapq.heappush(heap, (nxt[0] + 1, nxt[1]))
        if heap:
            if heap[0][0] < -1:
                return ""
            result.append(heap[0][1])
        return "".join(result)
