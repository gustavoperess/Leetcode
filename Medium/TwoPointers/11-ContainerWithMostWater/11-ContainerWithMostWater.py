from typing import List

class Solution:
    def maxAreaTLE(self, height: List[int]) -> int:
        #TLE
        ans = 0
        minheight = 0
        for i in range(len(height)):
            for y in range(i, len(height)):
                substring = height[i + 1:y + 1]
                if len(substring) > 0:
                    minheight = min(height[i], height[i + 1:y + 1][-1])
                    ans = max(ans, minheight * len((height[i + 1:y + 1])))

                
        return ans
    
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            h = min(height[l], height[r])
            ans = max(ans, h * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans



result = Solution()
result.maxArea( height = [1,8,6,2,5,4,8,3,7])
result.maxArea([4,3,2,1,4])
result.maxArea( height = [1,1])
result.maxArea([1,2,1])