from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashTable: dict = {}
        for i in logs:
            if i[0] in hashTable:
                hashTable[i[0]].append(i[1])
            else:
                hashTable[i[0]] = [i[1]]

        result = [0] * k
        an: dict = {}
        for key, value in hashTable.items():
            s = len(set(value))
            if s in an:
                an[s] += 1
            else:
                an[s] = 1
        
        for key, value in an.items():
            result[key - 1] = value
        return result
        
        



result = Solution()
result.findingUsersActiveMinutes( logs = [[1,1],[2,2],[2,3]], k = 4)
result.findingUsersActiveMinutes( logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5)