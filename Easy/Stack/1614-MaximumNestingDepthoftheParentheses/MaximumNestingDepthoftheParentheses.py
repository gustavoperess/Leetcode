

class Solution:
    def maxDepth(self, s: str) -> int:
        maxD = 0
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
            
            maxD = max(maxD, count)
        return maxD
            
            
            
            


result = Solution()
#result.maxDepth(s = "(1+(2*3)+((8)/4))+1")
result.maxDepth(s = "()(())((()()))")