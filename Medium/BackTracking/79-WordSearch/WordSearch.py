from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        path = set()

        def dfs(r, c, i):
                if i == len(word):
                    print(f"✅ Found word! Final path: {path}")
                    return True
                
                if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or (r, c) in path):
                    return False

                path.add((r, c))
                print(f"Step {i}: At ({r}, {c}) = '{board[r][c]}', Path so far: {path}")
                
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    print(f"  Exploring ({nr}, {nc}) from ({r}, {c})")
                    if dfs(nr, nc, i + 1):
                        return True

                print(f"🔙 Backtracking from ({r}, {c})")
                path.remove((r, c))
                return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

            


result = Solution()
t = result.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCEDE")
# t = result.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
print(t)
#result.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")