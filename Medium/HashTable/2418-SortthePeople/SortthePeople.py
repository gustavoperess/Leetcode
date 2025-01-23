from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result: dict = {}
        for i in range(len(names)):
            result[heights[i]] =  names[i]
        
        return (list(dict(sorted(result.items(), key=lambda x: x[0], reverse=True)).values()))
  




input = Solution()
result = input.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])
print(result)