from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums):
        freq = Counter(nums)
        
        def is_distinct():
            return all(v <= 1 for v in freq.values())

        if is_distinct():
            return 0
        
        k = 0
        while nums:
            if len(nums) < 3:
                return k + 1
            for i in range(3):
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            nums = nums[3:]
            k += 1
            if is_distinct():
                return k
        return k
    def minimumOperationsAnother(self, nums):
        count = 0
        while nums:
            if len(set(nums)) == len(nums):   
                break
            del nums[:3]
            count += 1
        print(count)
                     

      



result = Solution()
x = result.minimumOperationsAnother(nums = [1,2,3,4,2,3,3,5,7])
# t = result.minimumOperations(nums = [4,5,6,4,4])
