
from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def backtrack(start, path):
            count = 0
            if path:
                count += 1
            
            for i in range(start, len(nums)):
                if any(abs(nums[i] - x) == k for x in path):
                    continue
                path.append(nums[i])
                count += backtrack(i + 1, path)
                path.pop()
                
            return count

        return backtrack(0, [])

result = Solution()
result.beautifulSubsets(nums = [4,2,5,9,10,3], k = 1)#expected 23
#result.beautifulSubsets(nums = [2,4,6], k = 2)





