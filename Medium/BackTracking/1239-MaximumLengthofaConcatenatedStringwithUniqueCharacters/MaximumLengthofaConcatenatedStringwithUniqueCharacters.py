 
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        path = []

        def backtrack(i, used_chars):
            if len(arr) == i:
                print(path)
                return
      
            current = set(arr[i])

            if not current & used_chars:
                path.append(arr[i])
                backtrack(i + 1, used_chars | current)
                path.pop()
            
            backtrack(i + 1, used_chars)
       
        backtrack(0, set())  
        
          

result = Solution()
result.maxLength(["un","iq","ue"])
