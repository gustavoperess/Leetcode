


class Solution:
    def findTheLongestSubstringOne(self, s: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(len(s),0, -1):
            for j in range(len(s)-i+1):
                l=(s[j:j+i])
                odd = 0
                for k in "aeiou":
                    if(l.count(k)%2 !=0) :
                        odd = True
                        break
                if(not odd):
                    return i
            return 0
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        res = 0
        mask = 0
        mask_to_index = {0: -1}
        for i, v in enumerate(s):
            if v in vowels:
                mask = mask ^ (1 + ord(v) - ord('a'))
            if mask in mask_to_index:
                length = i - mask_to_index[mask]
                res = max(res, length)
            else:
                mask_to_index[mask] = i
        return res
            
result = Solution()
t = result.findTheLongestSubstring(s = "eleetminicoworoep")
print(t)
