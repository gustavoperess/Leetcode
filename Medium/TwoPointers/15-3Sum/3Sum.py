from collections import Counter
from typing import List

class Solution:
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        hashMap = {}
        for i in range(len(nums)):
            for y in range(len(nums)):
                for t in range(len(nums)):
                    if i != y and i != t and y != t:
                        if nums[i] + nums[y] + nums[t] == 0:
                            result = [nums[i], nums[y], nums[t]]
                            result.sort()
                            array_tuple = tuple(result)
                            if array_tuple not in hashMap:
                                hashMap[array_tuple] = result
        return list(hashMap.values())
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            l, r = n + 1, len(nums) - 1
            while l < r:
                treeSum = nums[n] + nums[l] + nums[r]
                if treeSum > 0:
                    r -= 1
                elif treeSum < 0:
                    l += 1
                else:
                    s = tuple(sorted([nums[n], nums[l], nums[r]])) 
                    ans.add(s)  
                    l += 1
                    r -= 1
        return list(ans)
        return ans
  


result = Solution()
#result.threeSum(nums = [-4, -1, -1, 0, 1, 2])
result.threeSum(nums=[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])