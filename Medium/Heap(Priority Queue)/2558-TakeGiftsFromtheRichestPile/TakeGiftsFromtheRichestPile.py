from typing import List
import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g = [-i for i in gifts]
        heapq.heapify(g)
        while k > 0:
            temp = math.floor(math.sqrt(-heapq.heappop(g)))
            heapq.heappush(g, -temp)
            k -= 1
          
        return sum(g) * -1
    
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        count = 0

        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                count += 1
                if count < 3:
                    ans += s[i]
            else:
                count = 1
                ans += s[i]
                    
        return ans


        
    
    

result = Solution()
# result.makeFancyString(s ="abbcccddddeeeee")
# result.pickGifts(gifts = [25,64,9,4,100], k = 4)
#result.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
#result.maxAverageRatio(classes = [[3,9],[4,5],[2,4],[2,10]], extraStudents = 4)
# result.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
#result.pickGifts(gifts = [1,1,1,1], k = 4)