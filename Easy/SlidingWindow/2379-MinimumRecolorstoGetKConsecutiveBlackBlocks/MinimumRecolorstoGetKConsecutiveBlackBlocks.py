
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, count = 0, 0
        ans = float("inf")
        for i in range(len(blocks)):
            if blocks[i] == "W":
                count += 1
            while i - l + 1 == k:
                ans = min(ans, count)
                if blocks[l] == "W":
                    count -= 1
                l += 1
    
        return ans
    
    

    
result = Solution()
#result.minimumRecolors(blocks = "WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", k = 15)
#result.minimumRecolors(blocks = "BWWWBB", k = 6)
result.minimumRecolors(blocks = "WBBWWBBWBW", k = 7)
