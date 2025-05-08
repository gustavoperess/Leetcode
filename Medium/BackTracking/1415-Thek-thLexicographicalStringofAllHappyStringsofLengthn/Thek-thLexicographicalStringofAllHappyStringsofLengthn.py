

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
        
    


result = Solution()
result.getHappyString(n = 1, k = 3)
result.getHappyString(n = 1, k = 4)
result.getHappyString(n = 3, k = 9)