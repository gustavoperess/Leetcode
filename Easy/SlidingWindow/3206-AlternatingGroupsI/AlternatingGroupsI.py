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
    
    # def numberOfAlternatingGroupsSecond(self, colors: List[int], k: int) -> int:        
    #     ans = 0
    #     n = len(colors)
        

    #     for r in range(n):  
    #         count = 0
    #         windown = [colors[(r + j) % n] for j in range(k)]  

    #         for l in range(k - 1):  
    #             if windown[l] != windown[l + 1]:
    #                 count += 1
    #             else:
    #                 break  
    #         if count + 1 == k:  
    #             ans += 1
     
    #     return ans
    
    def numberOfAlternatingGroupsSecond(self, colors: List[int], k: int) -> int:        
        ans = 0
        l = 0
        colors += colors
        for r in range(len(colors)):
            if r > 0 and colors[r] == colors[r - 1]:
                l = r
            if r - l + 1 >= k:
                ans += 1

        return ans
            
    
                
            

result = Solution()
#result.numberOfAlternatingGroupsTwo(colors=[0,1,0,0,1])
#result.numberOfAlternatingGroupsSecond( colors = [0,1,0,0,1], k = 3)

#result.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5])
#result.numberOfAlternatingGroupsSecond( colors = [0,1,0,0,1,0,1], k = 6)



