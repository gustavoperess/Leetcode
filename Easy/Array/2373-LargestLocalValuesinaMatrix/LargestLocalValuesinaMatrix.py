from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = nums.copy()
        occurrences = 0
        
        while occurrences < k:
            minValue = float('inf')
            position = -1
            first_occurrence_found = False
            
            for index, value in enumerate(result):
                if value < minValue:
                    minValue = value
                    position = index
                    first_occurrence_found = True
                elif value == minValue and not first_occurrence_found:
                    position = index
                    
              
            minValue *= multiplier
            result[position] = minValue
            occurrences += 1
        
        return result
    

              

result = Solution()
# result.getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2)
# result.getFinalState(nums = [1,2], k = 3, multiplier = 4)

result.getFinalState(nums = [5,3,1,1], k = 4, multiplier = 3)