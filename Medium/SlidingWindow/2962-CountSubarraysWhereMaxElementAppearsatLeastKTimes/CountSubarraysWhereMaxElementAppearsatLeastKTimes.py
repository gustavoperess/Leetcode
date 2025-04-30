
from typing import List
import math
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        hashMap = {}
        l = 0
        mValue = max(nums)
        ans = 0
        for r in range(len(nums)):
            if nums[r] in hashMap:
                hashMap[nums[r]] += 1
            else:
                hashMap[nums[r]] = 1
           
            while mValue in hashMap and hashMap[mValue] >= k:
                    ans +=  len(nums) - r
                    hashMap[nums[l]] -= 1
                    if hashMap[nums[l]] == 0:
                        del hashMap[nums[l]]
                    l += 1
              

        return ans
    
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            s = str(num)
            l = len(s) // 2
            
            if num > 10:
                if len(s) % 2 != 0:
                    continue
                
                left = sum(int(s[i]) for i in range(l))
                right = sum(int(s[i]) for i in range(l, len(s)))
            
                if left == right:
    
                    ans += 1
      
        return ans
    
    def mySqrt(self, x: int) -> int:
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            if mid > x // mid:
                last = mid - 1
            else: first = mid + 1

        return last
        

result = Solution()
result.mySqrt(x = 8)
#result.countSubarrays(nums = [1,3,2,3,3], k = 2)
