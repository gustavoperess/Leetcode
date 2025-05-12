from typing import List
from collections import defaultdict


class Solution:
    def findEvenNumbersTLE(self, digits: List[int]) -> List[int]:
            ans = []
            def dfs(path, used):
                if len(path) == 3:
                    x = "".join(path)
                    if x not in ans:
                        ans.append(x)
                    return

                for i, d in enumerate(digits):
                    if i in used:
                        continue
                    if not path and d == 0:
                        continue
                    if len(path) == 2 and d % 2 == 1:
                        continue
                    dfs(path + [str(d)], used | {i})
                
            dfs([], set())
            return sorted([int(i) for i in ans])
        
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        used = [False] * n
        ans = set()

        def dfs(path):
            if len(path) == 3:
                num = int("".join(map(str, path)))
                ans.add(num)
                return

            for i in range(n):
                if used[i]:
                    continue
                if len(path) == 0 and digits[i] == 0:
                    continue
                if len(path) == 2 and digits[i] % 2 == 1:
                    continue

                used[i] = True
                dfs(path + [digits[i]])
                used[i] = False

        dfs([])
        return sorted(ans)

    def findEvenNumbersHashMAp(self, digits: List[int]) -> List[int]:
        hmap, res  = defaultdict(int), []
        for num in digits:
            hmap[num] += 1
            
        for num in range(100, 999, 2):
            checker = defaultdict(int)
            for digit in str(num):
                checker[int(digit)] += 1
            
            if all(map(lambda x: x in hmap and checker[x] <= hmap[x], checker)):
                res.append(num)
        return res
        
result = Solution()
result.findEvenNumbersHashMAp(digits = [2,1,3,0])
#result.findEvenNumbers(digits = [2,2,8,8,2])