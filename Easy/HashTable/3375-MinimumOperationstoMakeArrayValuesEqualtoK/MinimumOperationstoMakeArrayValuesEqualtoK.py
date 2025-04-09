from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = min(nums)
        if m > k:
            return -1
        ans = 0
        s = set(nums)
        for i in s:
            if i  > k:
                ans += 1
                
        return ans
    
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            print(stack)
            while stack and (i == len(pattern) or pattern[i] == "I"):
                t = stack.pop()
                res.append(str(t))
           
        
        x = "".join(res)
        print(stack, res, x)


result = Solution()
result.minOperations( nums = [5,2,5,4,5], k = 2)
result.smallestNumber( pattern = "IIIDIDDD")
#result.smallestNumber( pattern = "DDD")