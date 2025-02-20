from typing import List



class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        subset = []
        def dfs(n, current=""):
            if len(current) == n:
                subset.append(current)
                return
            dfs(n , current + "0")
            dfs(n , current + "1")
         
        
        dfs(len(nums[0]), "")
            
   
        for s in subset:
            if s not in nums:
                return s
            
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        hashMap = {}
        count = 0
        for i in range(len(students)):
            if students[i][1] in hashMap:
                hashMap[students[i][1]].append(students[i][0])
            else:
                hashMap[students[i][1]] = [students[i][0]]

        for value in hashMap.values():
            t = len(set(value))
            count = max(t, count)
        return count
    
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        y = 0
        for i in range(len(boxes)):
            if boxes[i] == "0":
                print(i, y, len(boxes[i:]) - 1)
                
        y += 1


result = Solution()
result.minOperations(boxes = "001011")

