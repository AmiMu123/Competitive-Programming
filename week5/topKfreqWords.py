import heapq


class Solution:
    def topKFrequent(self, words, k):
        heap = []
        answer = []
        my_dict = dict()
        for word in words:
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1
        for key, value in my_dict.items():
            heapq.heappush(heap, [-1 * value, key])

        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer


obj = Solution()
print(obj.topKFrequent(['i', 'love', 'you', 'i', 'love', 'her'], 2))
