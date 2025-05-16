

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        for i in range(1, len(groups)):
            if groups[i] != groups[i - 1]:
                res.append(words[i])
        return res
    
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # if item has been seen before i remove the previous index with the new one
        # if never been seen i add it 
        seen = {}
        result = []
        for i in range(len(groups)):
            num = groups[i]
            if num in seen:
                old_index = seen[num]
                result.remove(old_index)
                result.append(i)
                seen[num] = i
            else:
                seen[num] = i
                result.append(i)
                
        ans = []                
        for i in result:
            ans.append(words[i])
        return ans

result = Solution()
result.getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2])
result.getWordsInLongestSubsequence(words = ["a","b","c","d"], groups = [1,2,3,4])
# print( len([1,0,1,1,1,1,1,1,1]), len(["a","b","c","d","e","f","g","h","i"]))
#result.getLongestSubsequence( words = ["e","a","b"], groups = [0,0,1])
#result.getLongestSubsequence( words = ["a","b","c","d","e","f","g","h","i"], groups = [1,0,1,1,1,1,1,1,0])
