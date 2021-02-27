from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        graph = defaultdict(list)
        res = []
        queue = deque()
        count_array = [0] * numCourses
        for edge in prerequisites:
            count_array[edge[0]] += 1
            graph[edge[1]].append(edge[0])
        change = None
        for i in count_array:
            if i == 0:
                queue.append(count_array.index(i))
                count_array[count_array.index(i)] = change
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for child in graph[curr]:
                count_array[child] -= 1
                if count_array[child] == 0:
                    queue.append(child)
                    count_array[child] = change
        if len(res) == numCourses:
            return True
        else:
            return False
