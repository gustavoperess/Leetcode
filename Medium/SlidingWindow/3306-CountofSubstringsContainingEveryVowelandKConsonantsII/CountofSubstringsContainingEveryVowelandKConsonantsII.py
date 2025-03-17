from collections import defaultdict


class Solution:
    def countOfSubstringsBruteFoce(self, word: str, k: int) -> int:
        # BRUTE FORCE 
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        ans = 0
        for i in range(n):
            for y in range(i, n):
                substring = word[i: y + 1]
                vowel_set = set()
                consonant_count = 0
                
                for char in substring:
                    if char in vowels:
                        vowel_set.add(char)
                    else:
                        consonant_count += 1
                if vowel_set == vowels and consonant_count == k:
                    ans += 1
    
        return ans
    
    def countOfSubstrings(self, word: str, k: int) -> int:
        # sliding windown approach
        def atleastK(k):
            hashMap = {}
            vowel_count = 0
            l = 0
            ans = 0
            for r in range(len(word)):
                if word[r] in "aeiou":
                    if word[r] in hashMap:
                        hashMap[word[r]] += 1
                    else:
                        hashMap[word[r]] = 1
                else:
                    vowel_count += 1
                
                while len(hashMap) == 5 and vowel_count >=k:
                    ans += (len(word) - r)
                    if word[l] in "aeiou":
                        hashMap[word[l]] -= 1
                    else:
                        vowel_count -= 1
                    if word[l] in hashMap:          
                        if hashMap[word[l]] == 0:
                            hashMap.pop(word[l])        
                    l += 1
            return ans
        return atleastK(k) - atleastK(k + 1)
    
   
        
result = Solution()
#result.countOfSubstrings(word = "ieaouqqieaouqq", k = 1)
