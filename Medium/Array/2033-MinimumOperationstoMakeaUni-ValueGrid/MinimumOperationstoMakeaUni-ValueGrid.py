from typing import List


class Solution:
    def minOperationsTLE(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([i for sublist in grid for i in sublist])
        medium = len(nums) // 2
        numberToSearch = nums[medium]
        count = 0
        for n in nums:
            while n != numberToSearch:
                if x == 0 or abs(n - numberToSearch) % x != 0:
                    return -1 
 
                if n < numberToSearch:
                    n += x        
                elif n > numberToSearch:
                    n -= x
                count += 1  
        
                      
        return count
        
    
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for n in row:
                arr.append(n)
                if n % x != grid[0][0] % x:
                    return False
        arr.sort()
        prefix = 0
        total = sum(arr)
        res = float("inf")
        for i in range(len(arr)):
            cost_left = arr[i] * i - prefix
            cost_right = total - prefix - (arr[i] * (len(arr) - i))
            operations = (cost_left + cost_right) // x
            res = min(res, operations)
            prefix += arr[i]
                   
        
        return res
    

    

result = Solution()
result.minOperations(grid = [[2,4],[6,8]], x = 2)
#result.minOperations(grid = [[1,2],[3,4]], x = 2)
#result.minOperations([[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]], 84)
#result.minOperations([[596,904,960,232,120,932,176],[372,792,288,848,960,960,764],[652,92,904,120,680,904,120],[372,960,92,680,876,624,904],[176,652,64,344,316,764,316],[820,624,848,596,960,960,372],[708,120,456,92,484,932,540]], 28)