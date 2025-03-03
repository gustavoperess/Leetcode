
from typing import List
from itertools import permutations 

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # left = []
        # center = []
        # right = []
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         left.append(nums[i])
        #     elif nums[i] > pivot:
        #         right.append(nums[i])
        #     else:
        #         center.append(nums[i])
        # return left + center + right
        
        left, rigth = 0, len(nums)
        ans = [0] * len(nums)
        mid_count = 0 
        i = 0
        while i < rigth:
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            elif nums[i] == pivot:
                mid_count += 1
            i += 1
        

        mid_end = left + mid_count
        while left < mid_end:
            ans[left] = pivot
            left += 1
            
        i = 0
        while i < rigth:
            if nums[i] > pivot:
                ans[left] = nums[i]
                left += 1
            i += 1
        
        print(ans)
                

    def validStrings(self, n: int) -> List[str]:
        ans = []
        
        def dfs(prev, string, n):
            if len(string) == n:
                ans.append(string)
                return
            
            dfs(1, string + "1", n)
            if prev == 1:
                dfs(0, string + "0", n)
            
        dfs(0, "0", n)
        dfs(1, "1", n)
     
        return print(ans)
     

        
        
result = Solution()
# result.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)
result.validStrings(n = 3)