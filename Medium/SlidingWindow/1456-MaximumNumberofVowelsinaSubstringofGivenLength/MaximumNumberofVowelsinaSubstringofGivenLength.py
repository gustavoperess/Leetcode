from typing import List

class Solution:    
    def maxVowels(self, s: str, k: int) -> int:
        hashMap = {}
        l = 0
        vowels = 'aeiou'
        ans = 0
        for r in range(len(s)):
            if s[r] in hashMap:
                hashMap[s[r]] += 1
            else:
                hashMap[s[r]] = 1
            
            while sum(hashMap.values()) >= k:
                t = sum(hashMap.get(v, 0) for v in vowels)
                ans = max(ans, t)
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
        return ans
    
    def maxVowelsTwo(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        curr_count, ans = 0, 0
        for r in range(len(s)):
            if r >= k:
                if s[r-k] in vowels:
                    curr_count -= 1
            if s[r] in vowels:
                curr_count += 1
            ans = max(ans, curr_count)
           
        return ans
    
    
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        current_cost, left , ans = 0,0,0
        for right in range(len(s)):
            current_cost += abs((ord(s[right]) - 97) - (ord(t[right]) - 97))
            while current_cost > maxCost:
                current_cost -= abs((ord(s[left]) - 97) - (ord(t[left]) - 97))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
              
               
               
                




        
        

result = Solution()
result.maxVowelsTwo(s = "abciiidef", k = 3)
#result.equalSubstring( s = "abcd", t = "bcdf", maxCost = 3)
# result.equalSubstring( s = "abcd", t = "cdef", maxCost = 3)
result.equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19)



