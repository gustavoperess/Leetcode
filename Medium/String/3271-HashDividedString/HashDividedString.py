
from typing import List
from itertools import permutations 
 
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = []
        prefix = 0
        for i, ch in enumerate(s):
            prefix += ord(ch)-97
            if (i+1) % k == 0:
                ans.append(chr(97 + prefix%26))
                prefix = 0  
        return ans
    
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            if words[i][:len(pref)] == pref:
                count += 1
        return count
    
    def isBalanced(self, num: str) -> bool:
        countEven = 0
        countOdd = 0
        for i in range(len(num)):
            if i % 2 == 0:
                countEven += num[i]
            else:
                countOdd += num[i]
        return countEven == countOdd

    def maximumOddBinaryNumber(self, s: str) -> str:
        p = permutations(s) 
        maxNumber = -1
        maxBinary = ""
        for i in p:
            n = "".join(i)
            k = int(n, 2)
            if k % 2 == 1:
                if k > maxNumber:
                    maxNumber = k
                    maxBinary = n
        return maxBinary
    
    def replaceDigits(self, s: str) -> str:
        ans = ["0"] * len(s)
        if s[-1].isalpha():
            ans[-1] = s[-1]
        for i in range(len(s) - 1):
            if i % 2 == 0:
                ans[i] = s[i]
                k = ord(s[i]) - 97 + int(s[i+1])
                u = chr(k + 97)
                ans[i + 1] = u
        print(ans)
         
        return "".join(ans)
        
result = Solution()
result.replaceDigits(s = "a1c1e1")
# result.stringHash(s = "mxz", k = 2)
#result.prefixCount(words = ["pay","attention","practice","attend"], pref = "at")



