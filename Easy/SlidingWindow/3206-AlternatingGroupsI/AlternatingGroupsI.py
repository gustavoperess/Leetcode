from typing import List



class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        # n ^ 2
        count = 0
        n = len(colors)
        for r in range(n):
            windown = [colors[(r + j) % n] for j in range(3)]
            if  windown[0] != windown[1] != windown[2]:
                count += 1
        return count
    
    def numberOfAlternatingGroupsTwo(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        colors += colors
        for i in range(n):
            if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
                ans += 1
        
        return ans





result = Solution()
result.numberOfAlternatingGroupsTwo(colors=[0,1,0,0,1])