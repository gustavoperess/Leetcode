from typing import List
import heapq, math

class Solution:
     
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = [-i for i in score]
        heapq.heapify(s)
        
        for i in range(len(s)):
            temp = -heapq.heappop(s)
            index = score.index(temp)
            if i == 0:
                score[index] = "Gold Medal"
            elif i == 1:
                score[index] = "Silver Medal"
            elif i == 2:
                score[index] = "Bronze Medal"
            else:
                x = str(i + 1)
                score[index] = x
   
        return score
        
        


result = Solution()
# result.pickGifts(gifts = [25,64,9,4,100], k = 4)
result.findRelativeRanks(score = [10,3,8,9,4])
#result.pickGifts(gifts = [1,1,1,1], k = 4)