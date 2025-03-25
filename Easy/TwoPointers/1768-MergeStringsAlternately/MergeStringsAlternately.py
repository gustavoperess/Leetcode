from typing import List
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        x = min(len(word1), len(word2))
        for i in range(x):
            ans += word1[i]
            ans += word2[i]
        if word1[x:] != "":
            ans += word1[x:]
        else:
            ans += word2[x:]
        return ans
    
    def mergeAlternatelySlidingWindownApproach(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ans = []
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
        
        ans.append(word1[i:])
        ans.append(word2[j:])
        return  "".join(ans)
    
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        k = 0
        while i < j:
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        nums[k] = nums[j]
        return k + 1
    


  

    


result = Solution()
result.mergeAlternatelySlidingWindownApproach( word1 = "ab", word2 = "pqrs")
result.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])

#result.removeDuplicates([1,1,2])