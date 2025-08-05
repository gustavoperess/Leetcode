
from typing import List
import heapq
import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for i, v in edges:
            graph[i].append(v)
            graph[v].append(i)

        queue = collections.deque([source])
        visited = set([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        print(queue, visited)
        return False


result = Solution()
#result.validPath( n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)
result.validPath( n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5)