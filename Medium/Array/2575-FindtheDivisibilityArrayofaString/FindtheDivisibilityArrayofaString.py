from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        result = [0] * len(word)
        prefix = ""
        for i in range(len(word)):
            prefix = 10*prefix + ord(word[i]) - 48
            prefix %= m
            if prefix == 0:
                result[i] = 1
            else:
                result[i] = 0
            
        return result
        
        
                

result = Solution()
result.divisibilityArray(word = "998244353", m = 3)
