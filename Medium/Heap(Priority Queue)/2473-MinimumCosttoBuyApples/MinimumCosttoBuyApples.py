
import collections
import heapq
from typing import List

class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        adj_list = collections.defaultdict(list)
        for u, v ,c in roads:
            v -= 1
            u -= 1
            adj_list[u].append((v, c))
            adj_list[v].append((u, c))
        
        heap = []
        best = appleCost[::]
        for i, c in enumerate(appleCost):
            heapq.heappush(heap, (c, i))
        
        while len(heap) > 0:
            d, index = heapq.heappop(heap)
            
            if d > best[index]:
                continue
            
            for v,cost in adj_list[index]:
                if best[index] + cost * (k + 1) < best[v]:
                    best[v] = best[index] + cost * (k + 1)
                    heapq.heappush(heap, (best[v], v))
    
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        heap = collections.defaultdict(list)
        tasks_count = collections.Counter()
        for i,v in tasks:
            heapq.heappush(heap[i], -v)
            tasks_count[v] += 1
        ans = 0
        for w in workers:
            if w in heap and len(heap[w]) > 0:
                p = abs(heapq.heappop(heap[w]))
                ans += p
                
                tasks_count[p] -= 1
                if tasks_count[p] == 0:
                    del tasks_count[p]
        
        print(tasks_count, heap)
     
    
                
                
        
        

result = Solution()
#result.minCost(n = 4, roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], appleCost = [56,42,102,301], k = 2)
result.maxProfit(workers = [1,2,3,4,5], tasks = [[1,100],[2,400],[3,100],[3,400]])
        



class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
      workers_tasks = collections.defaultdict(list)
      tasks_cnt = collections.Counter()

      total_profit = 0

      for skill, profit in tasks:
        heapq.heappush(workers_tasks[skill], -profit)
        tasks_cnt[profit] += 1

      for worker in workers:
        if worker in workers_tasks and len(workers_tasks[worker]) > 0:
          popped_profit = heapq.heappop(workers_tasks[worker])
          popped_profit = -popped_profit
          total_profit += popped_profit
          
          tasks_cnt[popped_profit] -= 1

          if tasks_cnt[popped_profit] == 0:
            del tasks_cnt[popped_profit]

      if tasks_cnt:
        total_profit += max(tasks_cnt.keys())

      return total_profit