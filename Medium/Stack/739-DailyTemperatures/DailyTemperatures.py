
from typing import List

class Solution:    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans

        
result = Solution()
result.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
