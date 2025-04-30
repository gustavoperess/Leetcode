from typing import List
# tried to do using recursion , got TLE , will come back to this someday
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:      
        def removen(nums):
            mi = float('inf')
            ma = float('-inf')
            for n in nums:
                if n:  
                    mi = min(mi, n[0]) 
                    ma = max(ma, n[0])
            return [mi, ma]
        
        if any(not n for n in nums):  
            return None  
        
        t = removen(nums)
        print(t)

        for n in nums:
            if t[0] in n:
                n.remove(t[0])
                next_range = self.smallestRange(nums)  
                if next_range:  
                    if (next_range[1] - next_range[0]) < (t[1] - t[0]):
                        return next_range  
        return t
    
    

result = Solution()
(result.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
