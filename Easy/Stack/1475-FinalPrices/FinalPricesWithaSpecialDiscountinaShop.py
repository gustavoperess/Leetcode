from typing import List

class Solution:
    def finalPricesBruteForce(self, prices: List[int]) -> List[int]:
        ans = prices[:]
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break 
        print(ans)
        return ans
    
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices[:]
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                ans[j] -= prices[i]
            stack.append(i)
        return ans
result = Solution()
#result.finalPrices(prices = [8,4,6,2,3])
#result.finalPrices([4,7,1,9,4,8,8,9,4])
result.finalPrices(prices = [10,1,1,6])