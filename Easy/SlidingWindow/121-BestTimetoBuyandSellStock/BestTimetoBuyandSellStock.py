from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l, r = 0, 1 
        
        while r < len(prices):
            if prices[r] > prices[l]:  #
                ans = max(ans, prices[r] - prices[l])
            else:
                l = r    
            r += 1  
        print(ans)
        return ans

result = Solution()
result.maxProfit(prices = [7,6,4,3,1])