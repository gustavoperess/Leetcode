
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        x = min(len(word1), len(word2))
        for i in range(x):
            ans += word1[i]
            ans += word2[i]
        if word1[x:] != "":
            ans += word1[x:]
        else:
            ans += word2[x:]
        return ans
    
    def mergeAlternatelySlidingWindownApproach(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ans = []
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
        
        ans.append(word1[i:])
        ans.append(word2[j:])
        return  "".join(ans)
    


result = Solution()
result.mergeAlternatelySlidingWindownApproach( word1 = "ab", word2 = "pqrs")