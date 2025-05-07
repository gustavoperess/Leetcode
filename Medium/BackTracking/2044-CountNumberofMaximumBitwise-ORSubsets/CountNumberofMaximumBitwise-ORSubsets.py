from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def OR(n):
            ans = n[0]
            for i in range(1, len(n)):
                ans |= n[i]
            
            return ans
        subsets = []
        maxNumber = 0
        result = 0
        def dfs(i):
            nonlocal maxNumber, result
            if i == len(nums):
                if len(subsets) > 0:
                    x = OR(subsets)
                    if x > maxNumber:
                        maxNumber = x
                        result = 1
                    elif x == maxNumber:
                        result += 1
                return 
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)
        t = dfs(0)
        return result


result = Solution()
result.countMaxOrSubsets(nums = [3,1])
result.countMaxOrSubsets(nums = [3,2,1,5])