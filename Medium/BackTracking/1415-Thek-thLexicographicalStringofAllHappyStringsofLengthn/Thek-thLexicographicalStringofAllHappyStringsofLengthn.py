
from typing import List

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        ans = []
        def dfs(path):
            if len(path) == n:
                ans.append("".join(path))
                return
            for c in chars:
                if path and c == path[-1]:
                    continue
                dfs(path + [c])
        
        dfs([])
        if k > len(ans):
            return ""
        return ans[k - 1]
        
    def letterCasePermutation(self, s: str) -> List[str]:
        
        substrings = []
        def dfs(path, i):
            if len(path) == len(s):
                substrings.append("".join(path))
                return
            if s[i].isalpha():
                dfs(path + [s[i].upper()], i + 1)
            dfs(path + [s[i]], i + 1)
             
        dfs([], 0)

        return substrings
                
       
       
result = Solution()
result.getHappyString(n = 1, k = 3)
result.letterCasePermutation(s = "a1b2")