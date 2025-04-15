from typing import List
import math
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        freq = {}
        for i in nums:
            complement = target - i
            if complement in freq:
                count += freq[complement]
            
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        return count

    def myd(self,m):
        y = math.floor(m/2)
        for i in range(10):
            y = m + y + i
        print(y)
        return y    
result  = Solution()
result.myd(5)
# result.twoSum(nums = [2,7,11,15], target = 9)
x = result.twoSum(nums=[1, 2, 3, 4, 3], target=6)
# t = result.twoSum(nums=[1, 5, 3, 3, 3], target=6)
