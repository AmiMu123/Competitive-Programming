from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        res = []
        queue = deque()
        count_array = [0] * numCourses
        for edge in prerequisites:
            parent = edge[1]
            child = edge[0]
            count_array[child] += 1
            if parent not in graph:
                graph[parent] = [child]
            else:
                graph[parent].append(child)

        change = None
        for i in count_array:
            if i == 0:
                queue.append(count_array.index(i))
                count_array[count_array.index(i)] = change

        while queue:
            curr = queue.popleft()
            res.append(curr)
            for parent, child in graph.items():
                if parent == curr:
                    for i in child:
                        count_array[i] -= 1
                        if count_array[i] == 0:
                            queue.append(i)
                            count_array[i] = change
        if len(res) == numCourses:
            return True
        else:
            return False
