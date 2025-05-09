class Solution:
    def countArrangementTLE(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]
        permutations = []
        subsets = []
   
        def dfs():
            if len(subsets) == len(nums):
                all_valid = True
                for k,v in enumerate(subsets):
                    key, value = int(k), int(v)
                    if (key + 1) % value != 0 and value % (key + 1) != 0:
                        all_valid = False
                        break
                if all_valid:
                    permutations.append(subsets.copy())
                  
                  
            for key, v in enumerate(nums):
                if v not in subsets:
                    subsets.append(v)
                    dfs()
                    subsets.pop()
        dfs()
        
        return len(permutations)
    
    def countArrangement(self, n: int) -> int:
        self.count = 0
        def backtrack(self, index, temp):
            if len(temp) == n:
                print(temp)
                self.count += 1
                return
            
            for number in range(1, n + 1):
                if number not in temp and (number % index == 0 or index % number == 0):
                    temp.append(number)              
                    backtrack(self, index + 1, temp)
                    temp.pop()
                  
          
        backtrack(self, 1, [])
        #print(self.count)
        return self.count
        

        
result = Solution()
result.countArrangement(n = 3)

print(4 * 3 * 2)