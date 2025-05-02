from typing import List

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        prev, result, n = 0, list(s), len(s)  
        for i in range(1, n):
            if s[i] == ".":
                continue
            if i - prev > 1:
                if s[prev] == s[i] :
                    for k in range(prev + 1, i):
                        result[k] = s[i]
                elif s[prev] == "R" and s[i] == "L":
                    l, r = prev + 1, i - 1
                    while l < r:
                        result[l] = "R"
                        result[r] = "L"
                        l += 1
                        r -= 1
            prev = i
        return "".join(result[1:-1])
    
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
        
        extra = 0
        curr  = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += customers[i]
        extra = curr
        for i in range(minutes, n):
            if grumpy[i] == 1:
                curr += customers[i]
            if grumpy[i - minutes] == 1:
                curr -= customers[i - minutes]
            extra = max(extra, curr)

        return base + extra
    
    
result = Solution()
#result.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3)
#result.maxSatisfied(customers = [9,7,6], grumpy = [1,1,1], minutes = 3)
result.maxSatisfied([2,2,7], [0,1,1], 3)

