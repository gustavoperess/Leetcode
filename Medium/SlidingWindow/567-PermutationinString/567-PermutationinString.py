from itertools import permutations 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = {}
        hashMapTwo = {}
        l = 0
        k = len(s1)
        for i in range(len(s1)):
            if s1[i] in hashMapTwo:
                hashMapTwo[s1[i]] += 1
            else:
                hashMapTwo[s1[i]] = 1 
       
        for r in range(len(s2)):
            if s2[r] in hashMap:
                hashMap[s2[r]] += 1
            else:
                hashMap[s2[r]] = 1
            
            while (r - l + 1) == k:
                if hashMap == hashMapTwo:
                    return True
                hashMap[s2[l]] -= 1
                if hashMap[s2[l]] == 0:
                    del hashMap[s2[l]]

                l += 1
        return False


result = Solution()
result.checkInclusion(s1 = "ab", s2 = "eidbaooo")