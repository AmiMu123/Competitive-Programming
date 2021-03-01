"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict


class Solution:
    def getImportance(self, employees, id: int) -> int:
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id] = (emp.subordinates, emp.importance)
        total_imp = [0]
        return self.dfs(graph, id, total_imp)

    def dfs(self, graph, id, total_imp):
        total_imp[0] += graph[id][1]
        for subord in graph[id][0]:
            self.dfs(graph, subord, total_imp)
        return total_imp[0]
