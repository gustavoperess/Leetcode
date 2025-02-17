
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        ans = [0] * l
        if k == 0:
            return ans
        if k > 0:
            ans[0]=wsum=sum(code[1:k+1])
            for i in range(1, l):
                r = (i + k) % l
                wsum+=-code[i]+code[r]
                ans[i]=wsum
        else:
            ans[0]=wsum=sum(code[-1:k-1:-1])
            for i in range(1, l):
                r = (i - k) % l
                wsum+=-code[-i]+code[-r]
                ans[-i]=wsum
        
        return ans
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        return maxSum / k
    
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            czero = 0
            cone = 0
            for y in range(i, len(s)):
                if s[y] == '0':
                    czero += 1
                else:
                    cone += 1
                if czero <= k or cone <= k:
                    ans += 1
        return ans
                
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)):
            t = prices[i - 1]
            print(t)

          
                
      


result = Solution()
result.maxProfit(prices = [7,1,5,3,6,4])
