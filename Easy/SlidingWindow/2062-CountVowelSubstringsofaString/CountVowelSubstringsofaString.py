from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        hashMap = defaultdict(int)
        ans = 0
        jj = j = 0  
        for r in range(len(word)):
            if word[r] in vowels:
                if r == 0 or word[r - 1] not in vowels:
                    jj = j = r
                    hashMap.clear()
                    
                hashMap[word[r]] += 1
                
                while len(hashMap) == 5 :
                    hashMap[word[j]] -= 1
                    if hashMap[word[j]] == 0:
                        del hashMap[word[j]]
                    j += 1
                
                ans += j - jj
     
        return ans
        