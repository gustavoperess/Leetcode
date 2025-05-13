
from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
    
            ans = ["0", "1"]
            res = []
            def backtrack(path):
                if len(path) == n:
                    res.append("".join(path))
                    return
                
                for i in range(len(ans)):
                    if path and path[-1] == '0' and ans[i] == '0':
                        continue
                    path.append(ans[i])
                    backtrack(path)
                    path.pop()
            
                        
                    
            backtrack([])
            return res


result = Solution()
result.validStrings(n = 2)