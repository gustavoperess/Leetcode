from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        visited = set()
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "." or (r, c) in visited :
                return 0
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        battleships = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X' and (r,c) not in visited:
                    dfs(r,c)
                    battleships += 1
                
                
        return battleships
            
        
        



result = Solution()
result.countBattleships(board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
result.countBattleships(board = [["."]])