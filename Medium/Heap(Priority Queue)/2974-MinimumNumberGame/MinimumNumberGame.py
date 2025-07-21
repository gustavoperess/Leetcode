from typing import List
import heapq
import math

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        i = len(nums)
        if i <= 1:
            return nums
        heapq.heapify(nums)
        arr = []
        while len(nums) > 1:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            arr.append(bob)
            arr.append(alice)
            
        return arr
    
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:       
        heap = [(y,x) for x,y in enumerate(nums)]
        heapq.heapify(heap)
        ans = nums[::]
        while k > 0:
            x, y = heapq.heappop(heap)
            ans[y] *= multiplier
            heapq.heappush(heap, (ans[y], y))
            k -= 1
        return ans
                
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
    
        for i,g in enumerate(grid): 
            l = len(g)
            x = [-i for i in g]
            heapq.heapify(x)
            for _ in range(l):
                s = abs(heapq.heappop(x))
            
    


result = Solution()
result.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2)
result.deleteGreatestValue(grid = [[1,2,4],[3,3,1]])

print(math.sqrt(225))
