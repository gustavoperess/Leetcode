from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        #x = (n * 2) - 1
        def dfs(path, count, index):
            if len(path) == (n * 2) - 1:
                return
       
            for number in range(1, n + 1):
                if number == 1 and count.get(1, 0) >= 1:
                    continue
                
                if number != 1 and count.get(number, 0) == 2:
                    continue
                
                if path and number > 1 and path[-1] == number:
                    continue
                    #print(path, path[-1], number, index)
                
                path.append(number)
                count[number] = count.get(number, 0 ) + 1
                
                dfs(path,count,  index + 1)
                
            
                path.pop()
                count[number] -= 1
        
            
        dfs([],{}, 0)     


    def subsetXORSum(self, nums: List[int]) -> int:
        self.result = 0
        def dfs(self,i, path, curr_number):
            if i == len(nums):
                self.result += curr_number
                return
            
            path.append(nums[i])
            dfs(self,i + 1, path, curr_number ^ nums[i])
            path.pop()
            dfs(self,i + 1, path, curr_number)
            
        
        
        dfs(self,0, [], 0)
      
      
        return self.result
    
   
        
        


result = Solution()
result.constructDistancedSequence(n=3)
result.subsetXORSum(nums = [5,1,6])
# result.subsetXORSum(nums = [1,3])








# [3,1,2,3,2]

# [0,1,2,3,4]