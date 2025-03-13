
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
    
    
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        for i in range(len(nums)):
            for y in range(i, len(nums)):
                substrings = nums[i:y + 1] 
                if set(substrings) == s:
                    count += 1
        return count            
                    
         
      
        
      

result = Solution()
#result.countCompleteSubarrays(nums = [5,5,5,5])
result.countCompleteSubarrays(nums = [1,3,1,2,2])