from typing import List

class Solution:
    def maxSubsequenceTwo(self, nums: List[int], k: int) -> List[int]:
        vals = [[i, nums[i]] for i in range(len(nums))]
        vals.sort(key=lambda  x: -x[1])
        vals = sorted(vals[:k])
        result =  [v for i,v in vals]
        return result
    
    def findWordsOne(self, words: List[str]) -> List[str]:
        firstRow = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        secondRow = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        thirdRow = ["z", "x", "c", "v", "b", "n", "m"]
        ans = []
        for i,v in enumerate(words):
            count1 = 0 
            count2 = 0
            count3 = 0
            for y in v:
                lowerCase = y.lower()
                if lowerCase in secondRow and lowerCase not in firstRow and lowerCase not in thirdRow:
                    count1 += 1
                    if count1 == len(v):
                        ans.append(v)
                        count1 = 0

                if lowerCase in firstRow and lowerCase not in secondRow and lowerCase not in thirdRow:
                    count2 += 1
                    if count2 == len(v):
                        ans.append(v)
                        count2 = 0
                
                if lowerCase in thirdRow and lowerCase not in firstRow and lowerCase not in secondRow:
                    count3 += 1
                    if count3 == len(v):
                        ans.append(v)
                        count3 = 0

              
    def findWords(self, words: List[str]) -> List[str]:
        l1="qwertyuiop"
        l2="asdfghjkl"
        l3="zxcvbnm"
        ans = []
        for i,v in enumerate(words):
            w = v.lower()
            if len(set(l1+w)) == len(l1) or len(set(l2+w)) ==len(l2) or len(set(l3+w)) ==len(l3):
                ans.append(v)
        return ans

                
            
            
                
        
    
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        s = sorted(nums)
        l = 0 
        hashMap = {}
        ans = float("-inf")
        result = []
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while r - l + 1 >= k:
                if sum(s[l:r + 1]) > ans:
                    ans = sum(s[l:r + 1])
                    result = s[l:r + 1]
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
        final_result = [0] * len(nums)
        for i,v in enumerate(nums):
            if v in result:
                result.remove(v)
                final_result[i] = v
            else:
                final_result[i] = ""

        return [i for i in final_result if i != ""]
                


result = Solution()
result.findWords(words = ["alaska", "dad", "popcorn"])
# result.findWords( words = ["adsdf","sfd"])
# result.maxSubsequence(nums = [2,1,3,3], k = 2)
# result.maxSubsequence(nums = [50, -75], k = 2)
# result.maxSubsequenceTwo( nums = [-1,-2,3,4], k = 3)
# result.maxSubsequence(nums = [3,4,3,3], k = 2)