from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(start: int, curr_sum: int, path: List[int]):
            if len(path) > k or curr_sum > n:
                return
            if len(path) == k and curr_sum == n:
                ans.append(path.copy())
                return
        
            
            for number in range(start, 10):
                if curr_sum + number > n:
                    break
                path.append(number)
                backtrack(number + 1, curr_sum + number, path)
                path.pop()
            
        
        backtrack(1, 0, [])
        print(ans)
        return ans
    

result = Solution()
#result.combinationSum3(k = 3, n = 7)
result.combinationSum3(k = 3, n = 9)

