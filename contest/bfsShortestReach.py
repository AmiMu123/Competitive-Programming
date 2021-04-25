#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the bfs function below.
from collections import deque, defaultdict


def bfs(n, m, edges, s):
    adjList = defaultdict(list)
    dist_map = dict()
    visited = set()
    result = []

    for edge in edges:
        adjList[edge[1]].append(edge[0])
        adjList[edge[0]].append(edge[1])

    queue = deque([(s, 0)])
    visited.add(s)
    while queue:
        node, dist = queue.popleft()
        dist_map[node] = dist
        for child in adjList[node]:
            if child not in visited:
                queue.append((child, dist + 6))
                visited.add(child)

    for i in range(1, n + 1):
        if i == s:
            continue
        if i not in dist_map:
            result.append(-1)
        else:
            result.append(dist_map[i])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
