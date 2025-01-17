from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = []
        final_result = 0
        for i in range(len(bank)):
            items = list(bank[i])
            counting = sum(1 for item in items if item == '1')
            if counting != 0:
                res.append(counting)
                
        for i in range(len(res) - 1):
            final_result += res[i] *res[i + 1]
        return final_result
        
result = Solution()
result.numberOfBeams(bank = ["011001","000000","010100","001000"])
result.numberOfBeams(bank = ["000","111","000"])