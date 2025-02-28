
from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monster = [0] * len(dist)
        
        for i in range(len(dist)):
            arrival = math.ceil(dist[i] / speed[i])
            
            if arrival < len(dist):
                monster[arrival] += 1
        eliminated = 0
        for i in range(len(dist)):
            if eliminated + monster[i] > i:
                print(eliminated, monster, monster[i], i)

            eliminated += monster[i]

    def minOperations(self, boxes: str) -> List[int]:
        balls = [0] * len(boxes)
        prefixCount = 0
        prefixSum = 0
        for i in range(len(boxes)):
            balls[i] = prefixCount * i - prefixSum
            if boxes[i] == '1':
                prefixCount += 1
                prefixSum += i
        
        suffixCount = 0
        suffixSum = 0
        for i in range(len(boxes) - 1, -1, -1):
            balls[i] += suffixSum - suffixCount * i
            if boxes[i] == "1":
                suffixCount += 1
                suffixSum += i
        
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0] * len(pref)
        res[0] = pref[0]
        xor_i = len(pref) - 1
        for i in range(len(pref) - 2, - 1, - 1):
            res[xor_i] = pref[i] ^ pref[i + 1]
            xor_i -= 1
        return res
            
result = Solution()
# result.minOperations(boxes = "001011")
result.findArray(pref = [5,2,0,3,1])

