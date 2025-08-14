from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            while heights[i] > stack[-1][1]:
                stack.pop()
            stack.append((i, heights[i]))
        ans = [i for i,v in stack]
        return ans


        



result = Solution()
#result.findBuildings(heights = [1,3,2,4])
# result.findBuildings(heights = [4,2,3,1])
result.findBuildings([6,88,57,20,51,49,36,35,54,63,62,46,3])
#result.findBuildings([2,2,2,2])
# result.findBuildings(heights = [4,3,2,1,5,1])