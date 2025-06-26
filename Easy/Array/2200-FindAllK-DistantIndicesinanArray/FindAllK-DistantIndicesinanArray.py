from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []

        for i in range(len(nums)):
            for y in range(len(nums)):
                if nums[y] == key and abs(i - y) <= k:
                        ans.append(i)
                        break
     
        return ans
                        
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        while len(s) % k:
            s += fill
        
        ans = []
        for i in range(0, len(s), k):
            elm = s[i:i + k]
            ans.append(elm)
        return ans
        
        



result = Solution()
#result.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)
#result.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2)
result.divideString( s = "abcdefghij", k = 3, fill = "x")