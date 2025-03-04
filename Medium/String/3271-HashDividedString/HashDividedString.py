
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

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        startY, startx = startPos
        for r in range(len(s)):
            x, y = startx, startY
            count = 0
            for c in range(r, len(s)):
                if s[c] == "R":
                    if x + 1 < n:
                        x += 1
                        count += 1
                    else:
                        break
                elif s[c] == "D":
                    if y + 1 < n:
                        y += 1
                        count += 1
                    else:
                        break
                elif s[c] == "L":
                    if x - 1 >= 0:
                        x -= 1
                        count += 1
                    else:
                        break
                elif s[c] == "U":
                    if y - 1 >= 0:
                        y -= 1
                        count += 1
                    else:
                        break
            ans.append(count)
                 
                
                
        print(ans)
            
result = Solution()
result.executeInstructions( n = 3, startPos = [0,1], s = "RRDDLU")
# result.stringHash(s = "mxz", k = 2)
#result.prefixCount(words = ["pay","attention","practice","attend"], pref = "at")