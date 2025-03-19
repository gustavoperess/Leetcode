



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMapOne = {}
        hasMapTwo = {}
        l = 0
        for i in range(len(t)):
            if t[i] in hashMapOne:
                hashMapOne[t[i]] += 1
            else:
                hashMapOne[t[i]] = 1
        
        for r in range(len(s)):
            if s[r] in hasMapTwo:
                hasMapTwo[s[r]] += 1
            else:
                hasMapTwo[s[r]] = 1
            
            # while (r + l - 1) < len(t):
            #     if s[l] in hashMapOne:
                    
            #         print(hashMapOne, hasMapTwo)
            #     l += 1    
        
    
             
        


result = Solution()
result.minWindow(s = "ADOBECODEBANC", t = "ABC")
result.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])