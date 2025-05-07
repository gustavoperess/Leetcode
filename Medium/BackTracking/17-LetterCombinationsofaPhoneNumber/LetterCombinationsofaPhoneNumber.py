from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        index = 0
        for digit in range(2, 10):
            if digit in [7, 9]:  
                count = 4
            else:
                count = 3
            map[str(digit)] = [letters[index + i] for i in range(count)]
            index += count
        
        result = []
        
        def dfs(index:int, path:str):
            if index == len(digits):
                result.append(path)
                return

            for l in map[digits[index]]:
                dfs(index + 1, path + l)
                
        dfs(0, "")
        
        return result

result = Solution()
result.letterCombinations(digits = "2")