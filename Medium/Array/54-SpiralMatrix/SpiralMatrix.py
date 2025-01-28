from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
#         directios = [[0, 1], [1, 0], [0, -1], [-1, 0]] #r, c
#         res = []
#         for row in range(len(matrix)):
#             for col in range(len(matrix[row])):
#                 print(matrix[row], matrix)
        
        
#         return res        
  



# result = Solution()
# # result.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
# result.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])



class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
    
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        items = []
        for i in points:
            items.append(i[0])
        items.sort()
        max_width = 0
        for i in range(len(items) - 1):
            max_width = max(max_width, items[i + 1] - items[i])
        return max_width
  
        
        
result = Solution()
result.countPairs(nums = [-1,1,2,3,1], target = 2)
# result.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]])
result.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])
