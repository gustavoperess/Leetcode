

from typing import List

class Solution:
    def threeConsecutiveOddOne(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False
    
    
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                count += 1
            else:
                count = 0
            
            if count == 3:
                return True
        return False
    
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        window = 0
        for i in range(min(3, len(arr))):
            window += arr[i] % 2
        if window == 3:
            return True
        for i in range(3, len(arr)):
            window += arr[i] % 2
            window -= arr[i - 3] % 2
            if window == 3:
                return True
        return False
        
       
        

result = Solution()
#result.threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12])
result.threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12])