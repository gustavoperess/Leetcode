from typing import List



class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans: dict = {}
        for i in range(len(l)):
            t = sorted(nums[l[i]: r[i] + 1])
            k = abs(t[0] - t[1])
            for y in range(len(t) - 1):
                result = abs(t[y] - t[y + 1])
                if result != k:
                    if i not in ans:
                        ans[i] = False
                        break
           
        for i in range(len(l)):
            if i not in ans:
                ans[i] = True
                
        return list(dict(sorted(ans.items())).values())
        
    
    




input = Solution()
result = input.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
print(result)