
from typing import List

class Solution:        
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
result.letterCasePermutation(s = "a1b2")