from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:        
        l, r = 0, 0
        n = len(boxes)
        ans = [0] 
        for i in range(1, n):
            if boxes[i] == "1":
                ans[0] += i
                r += 1
        if boxes[0] == "1":
            l = 1
        for i in range(1, n):
            ans.append(ans[i - 1] + l - r)
            if boxes[i] == "1":
                l += 1
                r -= 1
        print(ans)
    


result = Solution()
result.minOperations( boxes = "001011")