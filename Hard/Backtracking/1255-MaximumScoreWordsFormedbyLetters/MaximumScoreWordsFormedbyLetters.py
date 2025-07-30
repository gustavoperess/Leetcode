from typing import List
import math
from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCounter = Counter(letters)
        totalScore = 0
        def dfs(index, lettersCounter, currScore):
            nonlocal totalScore
            totalScore = max(totalScore, currScore)
            if index == len(words):
                return

            for i in range(index, len(words)):
                tmpCounter = lettersCounter.copy()
                word = words[i]
                wordScore = 0
                isValid = True
                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                if isValid:
                    dfs(i + 1, tmpCounter, currScore + wordScore)
              
        
        dfs(0, lettersCounter, 0)

        return totalScore

    
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        left = 0
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                if (nums[i] > nums[left] and nums[i] > nums[i + 1]) or \
                   (nums[i] < nums[left] and nums[i] < nums[i + 1]):
                    count += 1
                left = i
        return count 
    
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count,tosum = 0, 0
        for i in range(1, n + 1):
            if i not in banned and tosum + i <= maxSum:
                count += 1
                tosum += i
        return count
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        items = []         
        def dfs(node):
            if node == len(graph) -1:    
                ans.append(items[::])
                return
            
            for i in graph[node]:
                items.append(i)
                dfs(i)
                items.pop()
        items.append(0)  
        dfs(0)
       
result = Solution()
# #result.allPathsSourceTarget(graph = [[1,2],[3],[3],[]])
# result.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]])




def mistery(i, y, x):
    if i >= y:
        return True
    if x[i] != x[y]:
        return False
    return mistery(i + 1, y - 1, x)
   
x = [1,2,3,3,1]
answer = mistery(0, len(x) -1, x)
print(answer)