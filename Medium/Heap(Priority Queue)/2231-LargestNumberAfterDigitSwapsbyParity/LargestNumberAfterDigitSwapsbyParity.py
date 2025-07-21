from typing import List
import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(str(num))
        l, r = 0, len(nums) - 1
        r2 = len(nums)
  
        while l < r:
            while r2 > l + 1:
                left, right = int(nums[l]), int(nums[r2 - 1])
                if left % 2 == 0 and right % 2 == 0 and left < right:
                    nums[l],nums[r2 -1] = nums[r2-1], nums[l]
                if left % 2 == 1 and right % 2 == 1 and left < right:
                    nums[l],nums[r2-1] = nums[r2-1], nums[l]
                r2 -= 1
            r2 = len(nums)
            l += 1
        
        return int("".join(nums))

            
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = [(1 / y, 0, j + 1) for j, y in enumerate(arr[1:])]
        heapq.heapify(h)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(h)
            if i + 1 < j:
                heapq.heappush(h, (arr[i + 1] / arr[j], i + 1, j))
        return [arr[h[0][1]], arr[h[0][2]]]       
        
        

        


result = Solution()
result.largestInteger(65875)
result.kthSmallestPrimeFraction( arr = [1,2,3,5], k = 3)