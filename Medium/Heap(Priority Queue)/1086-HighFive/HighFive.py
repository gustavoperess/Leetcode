import heapq
from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashMap = {}
        for i in items:
            if i[0] in hashMap:
                hashMap[i[0]].append(i[1])
            else:
                hashMap[i[0]] = [i[1]]
        
        def sort_avg(list):
            list = sorted(list, reverse= True)
            return int(sum(list[0:5]) / 5)
        final = []
        for item in hashMap:
            final.append([item,sort_avg(hashMap[item])])
        return final
    
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            heapq.heappush(sticks, s1 + s2)
            ans += s1 + s2
 
        return ans
       


result = Solution()
# result.highFive(items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
#result.connectSticks(sticks = [2,4,3])
result.connectSticks(sticks = [1,8,3,5])
#result.highFive(items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]])
#result.highFive([[1,84],[1,72],[1,47],[1,43],[1,78],[2,79],[2,4],[2,23],[2,88],[2,79],[3,75],[3,80],[3,38],[3,73],[3,4]])