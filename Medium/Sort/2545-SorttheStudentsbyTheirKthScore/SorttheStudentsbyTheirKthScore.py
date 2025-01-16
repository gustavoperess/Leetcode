
from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        s = len(score)
        hashMap = {}
        for col in range(s):
            hashMap[col] = score[col][k]

        sortedItems = sorted(hashMap.items(), key=lambda x:x[1], reverse=True)
     
        finalResult = []
        for col in range(s):
            finalResult.append(score[sortedItems[col][0]])
        
        return finalResult
            

result = Solution()
result.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2)
# result.sortTheStudents(score = [[3,4],[5,6]], k = 0)
# result.sortTheStudents(score =[[64766,11978,20502,21365,79611,36797,58431,89540,59373,25955],[51305,66104,88468,5333,17233,32521,14087,42738,46669,65662],[93306,92793,54009,9715,24354,24895,20069,93332,73836,64359],[23358,84599,4675,20979,76889,34630,64098,23468,71448,17848]], k = 5)