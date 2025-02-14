
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
      


result = Solution()
# result.decrypt(code = [5,7,1,4], k = 3)
# result.decrypt(code = [2,4,9,3], k = -2)
result.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
