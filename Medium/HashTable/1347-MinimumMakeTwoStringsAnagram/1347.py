


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashTable: dict = {}
        for i in s:
            if i in hashTable:
                hashTable[i] +=  1
            else:
                hashTable[i] = 1
        
        for i in t:
            if i in hashTable:
                hashTable[i] -= 1
        
        
        count = 0
        for key, value in hashTable.items():
            if value > 0:
                count += value
        return count
        
        


result = Solution()
result.minSteps(s = "bab", t = "aba")
