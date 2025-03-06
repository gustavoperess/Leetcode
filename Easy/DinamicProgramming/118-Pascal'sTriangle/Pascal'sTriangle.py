from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows  -1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(left, right, parentheses):
            if left == n and right == n:
                ans.append(parentheses)
                return

            if left < n:
                dfs(left + 1, right, parentheses + "(")
            
            if right < left:
                dfs(left, right + 1, parentheses + ")")
            
        
        dfs(0, 0, "")    
        return ans

    def judgeCircle(self, moves: str) -> bool:
        x, y = [0,0]
        for m in moves:
            if m == "U":
                x += 1
            if m == "D":
                x -= 1
            if m == "L":
                y -= 1
            if m == "R":
                y += 1
        if x == 0 and y == 0:
            return True
        return False
        

      

